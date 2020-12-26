from ubuntu:20.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3 python3-pip && apt install libgl1-mesa-glx
ADD . /openCV/
RUN pip3 install -r /openCV/requirements.txt && chmod +x /openCV/start_services.sh
CMD /openCV/start_services.sh