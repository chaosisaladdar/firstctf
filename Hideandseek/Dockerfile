FROM tiangolo/uwsgi-nginx-flask:python3.6
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt
COPY ./app /app
EXPOSE 9999
CMD ["/app/run.sh"]
ENV UWSGI_INI /app/it_is_hard_t0_guess_the_path_but_y0u_find_it_5f9s5b5s9.ini
