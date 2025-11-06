FROM pandoc/extra:latest-ubuntu
LABEL maintainer=aleafs<aleafs@qq.com>

COPY . /app
#COPY temp/callout2latex/callout2latex.lua /app/filters/

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      python3 \
      python3-pip \
      vim wget unzip \
      imagemagick \
      librsvg2-bin \
      fonts-noto-color-emoji \
      fonts-firacode && \
    pip3 install PyYAML --break-system-packages && \
    wget https://github.com/adobe-fonts/source-han-sans/releases/download/2.005R/09_SourceHanSansSC.zip && \
    unzip 09_SourceHanSansSC.zip -d /usr/share/fonts

#COPY vimrc /etc/vim/vimrc.local

WORKDIR /app

ENTRYPOINT ["tail", "-f", "/dev/null"]
