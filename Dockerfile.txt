FROM eclipse-temurin:17-jre
WORKDIR /app
COPY . .
CMD ["java", "-Dnogui=true", "-jar", "JMusicBot-0.4.3-fix1.0.jar"]