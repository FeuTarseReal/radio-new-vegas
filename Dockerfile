FROM eclipse-temurin:17-jre
WORKDIR /app
COPY . .
CMD sh -c "echo 'token = '\"$TOKEN\" > config.txt && echo 'owner = 418516657775050762' >> config.txt && echo 'prefix = \"!\"' >> config.txt && java -Dnogui=true -jar JMusicBot-0.4.3-fix1.0.jar"