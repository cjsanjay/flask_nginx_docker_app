A rest api application build using Flask-restplus with basic auth
- Python PIL library wrapped inside Flask-restful interface
- A post call to the rest api with url of the publically accesible image will
invoke requested operation on to the image
- Included operations are: Blur, Greyscale, Flip, Invert, Line, Mask, Mirror, Pixelize,
   Sepia, SwapChannel, Xor

Pre-requisite: Docker and git installed on the system

Steps to deploy
- Clone git repository
   - git clone https://github.com/cjsanjay/flask_nginx_docker.git
- Move to flask_nginx_docker directory
   - cd flask_nginx_docker
- Run command
   - docker build -t flask_rest_app .
   - docker run -p 80:80 -t flask_rest_app
- Open browser and navigate to: http://0.0.0.0/api/
- Use swagger UI to interact with the api
- Username and password for auth: admin/password
- API post input request format:   
{  
  "id": 0,  
  "imageUrl": "string",  
  "imageLocalLocation": "string"  
}   

Just provide imageUrl value(something that is accessible over internet)

- Kill the container using(name will be load_app)
  - Docker ps (get the CONTAINER ID)
  - Docker kill CONTAINER ID
