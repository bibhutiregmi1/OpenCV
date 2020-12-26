from ubuntu:20.04
ENTRYPOINT []
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN python3 -m pip install
RUN pip install requirements.txt
ADD . /openCV/
RUN chmod +x /openCV/textDetect/start_services.sh
CMD /openCV/textDetect/start_services.sh