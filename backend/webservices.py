import os, os.path
import cherrypy
import MySQLdb
import datetime

db = MySQLdb.connect(host = "localhost",
                     user = "westory",
                     passwd = "spookit!",
                     db = "westory")
cur = db.cursor()


class WebServices(object):
    @cherrypy.expose
    def index(self):
        return "None"


class UserWebService(object):
    exposed = True
    
    @cherrypy.tools.accept(media = 'application/json')
    def POST(self, user, password, email, birthday = None, gender = None):
        query = "INSERT INTO users (userID, password, email, birthday, gender, date) VALUES ('%s', '%s', '%s', %s, %s, '%s')"
        
        if not birthday:
            birthday = "NULL"
        if not gender:
            gender = "NULL"

        query = query % (user,
                         password,
                         email,
                         birthday,
                         gender,
                         datetime.datetime.now())
        try:
            cur.execute(query)
            db.commit()
        except MySQLdb.Error, e:
            try:
                print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                print "MySQL Error: %s" % str(e)
                
    def GET(self, user):
        try:
            cur.execute("SELECT * FROM users WHERE userID='%s'" % user)
            results = cur.fetchone()

            if results:
                results = [str(entry) for entry in results]
                results = "|".join(results) + "\n"
                return results
            return "There is no match in the table 'users' where userID='%s'\n" % user
        except MySQLdb.Error, e:
            try:
                return "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                return "MySQL Error: %s" % str(e)

    def PUT(self, user):
        return "NOT IMPLEMENTED!\n"

    def DELETE(self, user):
        try:
            cur.execute("DELETE FROM users WHERE userID='%s'" % user)
            db.commit()
        except MySQLdb.Error, e:
            try:
                return "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                return "MySQL Error: %s" % str(e)


class StoriesWebService(object):
    exposed = True

    @cherrypy.tools.accept(media = 'text/plain')
    def POST(self, title, theme, description, user):
        query = "INSERT INTO stories (title, theme, description, date, userID) VALUES ('%s', '%s', '%s', '%s', '%s')"
        query = query % (title,
                         theme,
                         description,
                         datetime.datetime.now(),
                         user)
        try:
            cur.execute(query)
            db.commit()
            return
        except MySQLdb.Error, e:
            try:
                print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                print "MySQL Error: %s" % str(e)
        return "NOT IMPLEMENTED!"

    def GET(self, theme):
        query = "SELECT * FROM stories where theme='%s'"
        query = query % theme

        try:
            cur.execute(query)
            results = cur.fetchall()
            if results:
                return_str = '['
                # (name, theme, description, date, user)
                for result in results:
                    s = '{"name": "%s", "user": "%s", "date": "%s"}'
                    s = s % (result[0],
                             result[4],
                             result[3])
                    s += ","
                    return_str += s
                return_str = return_str[:-1] + "]"
            
                return return_str
            return "There is no match in the table 'stories' where theme='%s'\n" % theme
        except MySQLdb.Error, e:
            try:
                return "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                return "MySQL Error: %s" % str(e)

    def PUT(self, title):
        return "NOT IMPLEMENTED!\n"

    def DELETE(self, title):
        query = "DELETE FROM stories WHERE title='%s'"
        query = query % title
        try:
            cur.execute(query)
            db.commit()
        except MySQLdb.Error, e:
            try:
                return "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                return "MySQL Error: %s" % str(e)

class StoryWebService(object):
    exposed = True

    @cherrypy.tools.accept(media = 'text/plain')
    def GET(self, title):
        query_story = "SELECT * FROM stories WHERE title='%s'"
        query_story = query_story % title

        query_audios = "SELECT * FROM audio_files WHERE title='%s' order by date"
        query_audios = query_audios % title

        query_comments = "SELECT * FROM comments WHERE title='%s' order by date"
        query_comments = query_comments % title

        return_str = "["
        try:
            # (name, theme, description, date, user)
            cur.execute(query_story)
            results = cur.fetchone()
            audios = ""
            if results:
                s = '{"name": "%s", "user": "%s", "audios": ' % (results[0],
                                                                 results[4])
            else:
                s = '"None"'

            return_str += s
            
            
            # (filepath, user, title, date)
            cur.execute(query_audios)
            results = cur.fetchall()
            audios = "["
            audio_users = "["
            if results:
                for result in results:
                    audios += '"%s",' % result[0]
                    audio_users += '"%s",' % result[1]
                audios = audios[:-1]
                audio_users = audio_users[:-1]
            else:
                audios += '"None"'
                audio_users += '"None"'
            audios += "]"
            audio_users += "]"

            return_str += audios + ', "audio_users":' + audio_users + "}"

            comments = ""
            return_str += ',{"comments":'
            
            # (user, title, comment, date)
            cur.execute(query_comments)
            results = cur.fetchall()
            comments = "["
            if results:
                for result in results:
                    comments += '{"user": "%s", "date": "%s", "comment": "%s"},' % (result[0],
                                                                                    result[3],
                                                                                    result[2])
                comments = comments[:-1]
            else:
                comments += '"None"'
            comments += "]}]"

            return_str += comments
        except MySQLdb.Error, e:
            try:
                return "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                return "MySQL Error: %s" % str(e)
        else:
            return return_str
            
            

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"

    
if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
        },
        '/users': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
            'tools.CORS.on': True,
        },
        '/stories': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
            'tools.CORS.on': True,
        },
        '/story': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
            'tools.CORS.on': True,
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    webapp = WebServices()
    webapp.users = UserWebService()
    webapp.stories = StoriesWebService()
    webapp.story = StoryWebService()

    cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 9000})
    cherrypy.quickstart(webapp, '/', conf) 
    
