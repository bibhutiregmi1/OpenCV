from ubuntu:20.04
ENTRYPOINT []
RUN apt-get update
RUN apt-get install -y python3 python3-pip
ADD . /openCV/
RUN pip3 install -r /openCV/requirements.txt
RUN chmod +x /openCV/start_services.sh
CMD /openCV/textDetect/start_services.sh