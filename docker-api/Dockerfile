FROM php:8.2-apache

RUN apt-get update && apt-get install -y \
    libpng-dev libjpeg-dev libfreetype6-dev \
    libxml2-dev libzip-dev unzip \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install xml zip gd bcmath soap \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html

COPY Api-de-facturacion-electronica-sunat-Peru/ .

RUN mkdir -p files/facturacion_electronica/XML \
    files/facturacion_electronica/FIRMA \
    files/facturacion_electronica/PDF \
    files/qr \
    && chmod -R 777 files \
    && chmod -R 777 ws_sunat

EXPOSE 80
