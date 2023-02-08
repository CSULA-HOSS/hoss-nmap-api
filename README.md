# HOSS NMAP API

<h2>Deployment Instructions</h2>
<ol>
  <li>Push changes to git branch</li>
  <li>Connect to EC2 instance via SSH</li>
  <li>Pull latest changes to repo</li>
  <li>Change directory <code>cd 'hoss-nmap-api'</code></li>
  <li>Install requirements <code>sudo pip3 install -r requirements.txt</code></li>
  <li>Run project <code>sudo python3 main.py</code></li>
</ol>

<h3>Notes</h3>
<ol>
  <ul>Edit HOSS NMAP API Nginx config file: <code>sudo vim /etc/nginx/sites-enabled/hoss-api_nginx</code></ul>
  <ul>Edit Nginx config file: <code>sudo vim /etc/nginx/sites-enabled/hoss-api_nginx</code></ul>
  <ul>Restart Nginx: <code>sudo service nginx restart</code></ul>
  <ul>Start uvicorn server/project: <code>sudo python3 main.py </code> (Uvicorn is started programitcally)</ul>
</ol>

<h4>Additional Resources for deployment</h4>
<a href="https://www.youtube.com/watch?v=SgSnz7kW-Ko&t=534s">Youtube Video: How to Deploy FastAPI on AWS EC2: Quick and Easy Steps!</a>
<a href="https://www.uvicorn.org/deployment/#running-behind-nginx">Uvicorn deployment resources, Running Behinf Nginx</a>

