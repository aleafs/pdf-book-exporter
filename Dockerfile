FROM debian:latest
LABEL maintainer=aleafs<aleafs@qq.com>

COPY . /app
#COPY temp/callout2latex/callout2latex.lua /app/filters/

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      python3 \
      python3-pip \
      pandoc \
      vim wget unzip \
      imagemagick \
      librsvg2-bin \
      texlive-latex-base \
      texlive-latex-recommended \
      texlive-latex-extra \
      texlive-xetex \
      texlive-luatex \
      texlive-plain-generic \
      texlive-lang-chinese \
      texlive-lang-japanese \
      texlive-font-utils \
      texlive-fonts-recommended \
      fonts-noto-color-emoji && \
    pip3 install PyYAML --break-system-packages && \
    wget --progress=bar:force:noscroll https://github.com/adobe-fonts/source-han-sans/releases/download/2.005R/09_SourceHanSansSC.zip && \
    unzip 09_SourceHanSansSC.zip -d /usr/share/fonts && \
    rm -f 09_SourceHanSansSC.zip && \
    wget --progress=bar:force:noscroll -O/usr/share/fonts/SourceHanMono.ttc https://github.com/adobe-fonts/source-han-mono/releases/download/1.002/SourceHanMono.ttc && \
    ln -f -s /app/vimrc /etc/vim/vimrc.local && \
    echo "alias ll='ls -l --color=auto'" >> /root/.bashrc

WORKDIR /app

ENTRYPOINT ["tail", "-f", "/dev/null"]
