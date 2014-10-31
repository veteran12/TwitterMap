TwitterMap
==========
I developed this website in order to get familiar with aws ec2, dynamodb, elastic beanstalk.
skills, js, jquery, ajax, json, Django, python, aws ec2, dynamodb, elastic beanstalk, googlemap api v3 etc.

This project is to build a website which can accept a key word and then display the position of tweets that contain this keywords.
1,The website is build with Django.
2,I wrote several python files to retrieve data using twitter streaming api and then persist the data into dynamodb.
3,I use aws elastic beanstalk to deploy the website.

You can see this website via this link, http://twittermap-env-23t6unfgmj.elasticbeanstalk.com/index/

note,
1, I use json format file to transfer data between twitter, data files, front end pages, backend server. 
for js, I use a lib function from Jquery to call backend service,
$.getJSON(require, parameter, data)

$(document).ready(function(){
      $("button").click(function(){
        var x=eval(document.getElementById('keyword')).value
        var require = '../search/keyword'
        var keyword = {keyword : x}
        $.getJSON(require, keyword,
            function(data) {
              //alert(data[1][0])
              var locations = new Array();
              for (var key in data) {
                //alert(data[key][0])
                var geo = new Array(data[key][0], data[key][1], data[key][2]);
                locations.push(geo);
              }
              showPine(locations)
            });
      });
      
  2, At backend, in views.py fucntion search(), this code is to return data to frontend in jason format
    jsondata = simplejson.dumps(coordinates)
    return HttpResponse(jsondata, content_type="application/json")
    
  3, In order to search the keyword in dynamodb, I use scan function provided by aws dynamodb api "boto.dynamodb2"
  result = tweetMap.scan(text__contains=keyword)
  
  4, As for using beanstalk, the initialised instance just have python2.7, other python lib needed must be decleared in 
  requirements.txt which must be located in the top diractory of you wensite, then beanstalk can install those lib via 
  pip command

172-16-181-222:twittermap zhangtong$ cat requirements.txt 
Django==1.7.1
PyRSS2Gen==1.0.0
Twisted==12.2.0
bdist-mpkg==0.4.4
boto==2.34.0
httplib2==0.9
oauth2==1.5.211
python-dateutil==1.5
simplejson==3.6.5
wsgiref==0.1.2
xattr==0.6.4
172-16-181-222:twittermap zhangtong$

  5, before uploading the app, some file need to be checked,
---twittermap.config must be build in .ebextensions/
---double check optionsettings.twittermap-env
[aws:elasticbeanstalk:container:python]
NumProcesses=1
NumThreads=15
StaticFiles=/static/=static/
WSGIPath=twittermap/wsgi.py //must be this!!!
---in file settings.py
some configuration need to modified
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'tmap/templates'),
    '/Users/zhangtong/Desktop/CLOUD_COMPUTING/twittermap/tmap/templates',
)

  5, In order to let the application deployed on beanstalk can access dynamodb, a role granted to access dynamodb must be
  build. The role policy like this
  {
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:BatchGetItem",
        "dynamodb:Scan"
       ],
      "Resource": "arn:aws:dynamodb:us-east-1:020839080619:table/*"
    }
  ]
}
Bind this role to your instance, then just use "conn = boto.connect_dynamodb()" in your application to connect dynamodb. 

to be continue :-)

Improve,the data now is not in real time, I will improve to catch the twitter data in real time!


  
  
  
