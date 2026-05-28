#!/bin/sh
set -e

cat > /var/www/html/.env << EOL
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
