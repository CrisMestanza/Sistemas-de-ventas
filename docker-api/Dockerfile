# syntax=docker/dockerfile:1
FROM php:8.2-cli

RUN apt-get update && apt-get install -y \
    libpng-dev libjpeg-dev libfreetype6-dev \
    libxml2-dev libzip-dev unzip git \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install pdo_mysql xml zip gd bcmath \
    && rm -rf /var/lib/apt/lists/*

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/html

COPY composer.json composer.lock ./
RUN composer install --no-dev --optimize-autoloader --no-scripts

COPY . .
RUN composer dump-autoload --optimize
RUN mkdir -p storage/framework/sessions storage/framework/views storage/framework/cache \
    storage/logs bootstrap/cache \
    && chmod -R 775 storage bootstrap/cache

COPY <<'EOF' /usr/local/bin/docker-entrypoint.sh
#!/bin/sh
set -e

cat > /var/www/html/.env <<EOL
APP_NAME="API Facturacion SUNAT"
APP_ENV=production
APP_KEY=
APP_DEBUG=false
APP_URL=http://localhost:8001

LOG_CHANNEL=stack
LOG_LEVEL=error

DB_CONNECTION=mysql
DB_HOST=${DB_HOST:-db}
DB_PORT=${DB_PORT:-3306}
DB_DATABASE=${DB_DATABASE:-apigo}
DB_USERNAME=${DB_USERNAME:-root}
DB_PASSWORD=${DB_PASSWORD:-}

CACHE_DRIVER=file
SESSION_DRIVER=file
QUEUE_CONNECTION=sync
EOL

php artisan key:generate --force
php artisan config:clear
php artisan migrate --force
exec php artisan serve --host=0.0.0.0 --port=8001
EOF

RUN chmod +x /usr/local/bin/docker-entrypoint.sh

EXPOSE 8001
ENTRYPOINT ["docker-entrypoint.sh"]
