from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too
#fieds_name= ["username", "password", "verify-password", "email"]

@app.route('/')
def signup():
          return render_template('signup.html')
@app.route('/', methods=['POST'])
def confirm_signup():
          username = request.form['username']
          password= request.form['password']
          verify_password= request.form['verify_password']
          email= request.form['email']
##          uvalid=False
##          pvalid=False
##          pvvalid=False
##          evalid=False
##            
##          if len(username)==0 or len(username) not in range(3, 21) or username.find(' ')!=-1:
##                  return uvalid
##                  #error = "The '{0}' have not to be empty and has no space.The length has not to be out of the range 3 to 21".format("username")
##                  #return redirect("/?error=" + error)
##          if len(password) not in range(3, 21) or password.find(' ')!=-1 :
##                  #error = "The '{0}' has not to be empty and has no space.The length has not to be out of the range 3 to 21 and '{1}' must match the given '{2}'".format("password", "verify_password", "password" )
##                  #return redirect("/?error=" + error)
##                  return pvalid
##          if  verify_password!=password:
##                return pvvalid
##          
##      
##          if len(email) not in range(3, 21) or email.find("@")==-1 or email.find(".")==-1 or email.find(" ")!=-1:
##                    #error = "The '{0}'must contain '{1}' has no space .It must be 3 to 21 character length ".format("email","@ .")
##                    #return redirect("/?error=" + error)
##                    return evalid
                  
          ##Redirection if error
          #if uvalid:
          if len(username)==0 or len(username) not in range(3, 21) or username.find(' ')!=-1:
                    error = "The '{0}' have not to be empty and has no space.The length has not to be out of the range 3 to 21".format("username")
                    return redirect("/?error=" + error)
          else:
                    if len(password) not in range(3, 21) or password.find(' ')!=-1 : 
                              error = "The '{0}'length has not to be out of the range 3 to 21 and '{1}' must match the given '{2}'".format("password", "verify_password", "password")
                              return redirect("/?error=" + error)
                    else:
                              if verify_password!=password:
                                        error = "The '{0}'must match the entered '{1}'".format("verify_password",  "password")
                                        return redirect("/?error=" + error)
                              else:
                                         if len(email) not in range(3, 21) or email.find("@")==-1 or email.find(".")==-1 or email.find(" ")!=-1:
                                         #if evalid:
                                              error = "The '{0}'must contain '{1}' has no space .It must be 3 to 21 character length ".format("email","@ .")
                                              return redirect("/?error=" + error)
                                         else:
                                                  if (len(username)  in range(3, 21) and username.find(' ')==-1) and (len(password)  in range(3, 21) and password.find(' ')==-1) and (verify_password==password) and (len(email) in range(3, 21) and email.find("@")!=-1 and email.find(".")!=-1 and email.find(" ")==-1):
                                              #if not uvalid and not pvalid and not evalid():
                                                        return  render_template('confirm01.html', username= username, email= email)
                                                  else:
                                                        if (len(username)  in range(3, 21) and  username.find(' ')==-1) and (len(password) in range(3, 21) and password.find(' ')==-1) and (verify_password==password) and len(email)==0:
                                                                  no_email='not entered!'
                                                                  return  render_template('confirm01.html', username= username, email= no_email)
app.run()
