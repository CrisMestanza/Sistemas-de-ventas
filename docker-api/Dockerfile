FROM php:8.2-cli

RUN apt-get update && apt-get install -y \
    libpng-dev libjpeg-dev libfreetype6-dev \
    libxml2-dev libzip-dev unzip git \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install pdo_mysql xml zip gd bcmath soap \
    && rm -rf /var/lib/apt/lists/*

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/html

COPY Api-de-facturacion-electronica-sunat-Peru/composer.json Api-de-facturacion-electronica-sunat-Peru/composer.lock ./
RUN composer install --no-dev --optimize-autoloader --no-scripts

COPY Api-de-facturacion-electronica-sunat-Peru/ .
RUN composer dump-autoload --optimize
RUN mkdir -p storage/framework/sessions storage/framework/views storage/framework/cache \
    storage/logs bootstrap/cache \
    && chmod -R 775 storage bootstrap/cache

COPY Sistemas-de-ventas/docker-api/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

EXPOSE 8001
ENTRYPOINT ["docker-entrypoint.sh"]
