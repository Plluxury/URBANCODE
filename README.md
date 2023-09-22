**its working repo for URBANCODE**

HOW TO RUN

# You need installed docker on yout local machine !

# only what you need just run dockerfile and see result

first: docker build -it hackaton .

second: docker run -it hackaton

third: check docker id -> docker ps

fourth: docker exec -it <docker_id> /bin/bash

fifth: cd result

In dir result wil be all .txt for images in train_data/images/val 
which contains records in format: class confidence xmin ymin xmax ymax

You can open .txt file with: cat file_name.txt