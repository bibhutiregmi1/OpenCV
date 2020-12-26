from ubuntu:20.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache -- upgrade pip && pip3 install requirements.txt
ADD . /openCV/
RUN chmod +x /openCV/textDetect/start_services.sh
CMD /openCV/textDetect/start_services.sh