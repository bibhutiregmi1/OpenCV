from ubuntu:20.04
ENTRYPOINT []
RUN pip install requirements.txt
ADD . /openCV/
RUN chmod +x /openCV/textDetect/start_services.sh
CMD /openCV/textDetect/start_services.sh