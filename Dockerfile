from ubuntu:20.04
ENTRYPOINT []
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt
ADD . /openCV/
RUN chmod +x /openCV/textDetect/start_services.sh
CMD /openCV/textDetect/start_services.sh