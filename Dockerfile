#Use python as base image
FROM python:3.9-slim

#Use working directory /app
WORKDIR /app

#Copy all the content of current directory to /app
#ADD kg_construction_triplets.py /app
#ADD needed_files/relation2id.txt /app
#ADD needed_files/w2id.txt /app
ADD . /app
#ADD saved_models/best_re_model/tut2-model_ner.pt /app
#ADD saved_models/best_re_model/tensors.pt /app
#ADD saved_models/best_ner_model/. /app
RUN /usr/local/bin/python -m pip install --upgrade pip
#Installing required packages
RUN pip install -r requirements.txt

#Open port 5000
EXPOSE 5000

#Set environment variable
ENV NAME OpentoAll

#Run python program
CMD ["python","kg_construction_triplets.py"]


