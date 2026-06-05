-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: facsiswave
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=137 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add subir documento imagen',7,'add_subirdocumentoimagen'),(26,'Can change subir documento imagen',7,'change_subirdocumentoimagen'),(27,'Can delete subir documento imagen',7,'delete_subirdocumentoimagen'),(28,'Can view subir documento imagen',7,'view_subirdocumentoimagen'),(29,'Can add categoria',8,'add_categoria'),(30,'Can change categoria',8,'change_categoria'),(31,'Can delete categoria',8,'delete_categoria'),(32,'Can view categoria',8,'view_categoria'),(33,'Can add clientes',9,'add_clientes'),(34,'Can change clientes',9,'change_clientes'),(35,'Can delete clientes',9,'delete_clientes'),(36,'Can view clientes',9,'view_clientes'),(37,'Can add codigo correo',10,'add_codigocorreo'),(38,'Can change codigo correo',10,'change_codigocorreo'),(39,'Can delete codigo correo',10,'delete_codigocorreo'),(40,'Can view codigo correo',10,'view_codigocorreo'),(41,'Can add compra detalle',11,'add_compradetalle'),(42,'Can change compra detalle',11,'change_compradetalle'),(43,'Can delete compra detalle',11,'delete_compradetalle'),(44,'Can view compra detalle',11,'view_compradetalle'),(45,'Can add compras',12,'add_compras'),(46,'Can change compras',12,'change_compras'),(47,'Can delete compras',12,'delete_compras'),(48,'Can view compras',12,'view_compras'),(49,'Can add departamentos',13,'add_departamentos'),(50,'Can change departamentos',13,'change_departamentos'),(51,'Can delete departamentos',13,'delete_departamentos'),(52,'Can view departamentos',13,'view_departamentos'),(53,'Can add detallecategoriaxunidades',14,'add_detallecategoriaxunidades'),(54,'Can change detallecategoriaxunidades',14,'change_detallecategoriaxunidades'),(55,'Can delete detallecategoriaxunidades',14,'delete_detallecategoriaxunidades'),(56,'Can view detallecategoriaxunidades',14,'view_detallecategoriaxunidades'),(57,'Can add detalletipousuarioxmodulos',15,'add_detalletipousuarioxmodulos'),(58,'Can change detalletipousuarioxmodulos',15,'change_detalletipousuarioxmodulos'),(59,'Can delete detalletipousuarioxmodulos',15,'delete_detalletipousuarioxmodulos'),(60,'Can view detalletipousuarioxmodulos',15,'view_detalletipousuarioxmodulos'),(61,'Can add distritos',16,'add_distritos'),(62,'Can change distritos',16,'change_distritos'),(63,'Can delete distritos',16,'delete_distritos'),(64,'Can view distritos',16,'view_distritos'),(65,'Can add lotes',17,'add_lotes'),(66,'Can change lotes',17,'change_lotes'),(67,'Can delete lotes',17,'delete_lotes'),(68,'Can view lotes',17,'view_lotes'),(69,'Can add modopago',18,'add_modopago'),(70,'Can change modopago',18,'change_modopago'),(71,'Can delete modopago',18,'delete_modopago'),(72,'Can view modopago',18,'view_modopago'),(73,'Can add modulos',19,'add_modulos'),(74,'Can change modulos',19,'change_modulos'),(75,'Can delete modulos',19,'delete_modulos'),(76,'Can view modulos',19,'view_modulos'),(77,'Can add numserie',20,'add_numserie'),(78,'Can change numserie',20,'change_numserie'),(79,'Can delete numserie',20,'delete_numserie'),(80,'Can view numserie',20,'view_numserie'),(81,'Can add producto',21,'add_producto'),(82,'Can change producto',21,'change_producto'),(83,'Can delete producto',21,'delete_producto'),(84,'Can view producto',21,'view_producto'),(85,'Can add proveedores',22,'add_proveedores'),(86,'Can change proveedores',22,'change_proveedores'),(87,'Can delete proveedores',22,'delete_proveedores'),(88,'Can view proveedores',22,'view_proveedores'),(89,'Can add provincias',23,'add_provincias'),(90,'Can change provincias',23,'change_provincias'),(91,'Can delete provincias',23,'delete_provincias'),(92,'Can view provincias',23,'view_provincias'),(93,'Can add tipocliente',24,'add_tipocliente'),(94,'Can change tipocliente',24,'change_tipocliente'),(95,'Can delete tipocliente',24,'delete_tipocliente'),(96,'Can view tipocliente',24,'view_tipocliente'),(97,'Can add tipodocumento',25,'add_tipodocumento'),(98,'Can change tipodocumento',25,'change_tipodocumento'),(99,'Can delete tipodocumento',25,'delete_tipodocumento'),(100,'Can view tipodocumento',25,'view_tipodocumento'),(101,'Can add tipo entidad',26,'add_tipoentidad'),(102,'Can change tipo entidad',26,'change_tipoentidad'),(103,'Can delete tipo entidad',26,'delete_tipoentidad'),(104,'Can view tipo entidad',26,'view_tipoentidad'),(105,'Can add tipo igv',27,'add_tipoigv'),(106,'Can change tipo igv',27,'change_tipoigv'),(107,'Can delete tipo igv',27,'delete_tipoigv'),(108,'Can view tipo igv',27,'view_tipoigv'),(109,'Can add tipousuario',28,'add_tipousuario'),(110,'Can change tipousuario',28,'change_tipousuario'),(111,'Can delete tipousuario',28,'delete_tipousuario'),(112,'Can view tipousuario',28,'view_tipousuario'),(113,'Can add unidades',29,'add_unidades'),(114,'Can change unidades',29,'change_unidades'),(115,'Can delete unidades',29,'delete_unidades'),(116,'Can view unidades',29,'view_unidades'),(117,'Can add usuario',30,'add_usuario'),(118,'Can change usuario',30,'change_usuario'),(119,'Can delete usuario',30,'delete_usuario'),(120,'Can view usuario',30,'view_usuario'),(121,'Can add venta',31,'add_venta'),(122,'Can change venta',31,'change_venta'),(123,'Can delete venta',31,'delete_venta'),(124,'Can view venta',31,'view_venta'),(125,'Can add venta detalle',32,'add_ventadetalle'),(126,'Can change venta detalle',32,'change_ventadetalle'),(127,'Can delete venta detalle',32,'delete_ventadetalle'),(128,'Can view venta detalle',32,'view_ventadetalle'),(129,'Can add empresa',33,'add_empresa'),(130,'Can change empresa',33,'change_empresa'),(131,'Can delete empresa',33,'delete_empresa'),(132,'Can view empresa',33,'view_empresa'),(133,'Can add empleado',34,'add_empleado'),(134,'Can change empleado',34,'change_empleado'),(135,'Can delete empleado',34,'delete_empleado'),(136,'Can view empleado',34,'view_empleado');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `caja`
--

DROP TABLE IF EXISTS `caja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caja` (
  `id_caja` int NOT NULL AUTO_INCREMENT,
  `fecha_apertura` date DEFAULT NULL,
  `hora_apertura` time DEFAULT NULL,
  `fecha_cierre` date DEFAULT NULL,
  `hora_cierre` time DEFAULT NULL,
  `monto_inicial` decimal(10,2) DEFAULT NULL,
  `monto_final` decimal(10,2) DEFAULT NULL,
  `estado` int DEFAULT NULL,
  `usuario_apertura` int DEFAULT NULL,
  `usuario_cierre` int DEFAULT NULL,
  PRIMARY KEY (`id_caja`),
  KEY `fk_usaurio_apertura_idx` (`usuario_apertura`),
  KEY `fk-Usuario_cierre_idx` (`usuario_cierre`),
  CONSTRAINT `fk_usaurio_apertura` FOREIGN KEY (`usuario_apertura`) REFERENCES `usuario` (`idusuario`),
  CONSTRAINT `fk_usuario_cierre` FOREIGN KEY (`usuario_cierre`) REFERENCES `usuario` (`idusuario`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caja`
--

LOCK TABLES `caja` WRITE;
/*!40000 ALTER TABLE `caja` DISABLE KEYS */;
INSERT INTO `caja` VALUES (24,'2026-05-29','16:51:26',NULL,NULL,10.00,NULL,1,2,NULL);
/*!40000 ALTER TABLE `caja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `idcategoria` int NOT NULL AUTO_INCREMENT,
  `nomcategoria` varchar(255) NOT NULL,
  `estado` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`idcategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (27,'Lacteos',1),(28,'Bebidas',1);
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `idcliente` int NOT NULL AUTO_INCREMENT,
  `idtipocliente` int NOT NULL,
  `numdoc` varchar(25) DEFAULT NULL,
  `razonsocial` varchar(255) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `estado` int DEFAULT '1',
  `id_tipo_entidad` int DEFAULT NULL,
  PRIMARY KEY (`idcliente`),
  KEY `idtipocliente` (`idtipocliente`),
  KEY `fk_tipo_entidad_idx` (`id_tipo_entidad`),
  CONSTRAINT `fk_tipo_entidad` FOREIGN KEY (`id_tipo_entidad`) REFERENCES `tipo_entidad` (`id_tipo_entidad`)
) ENGINE=InnoDB AUTO_INCREMENT=232 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (220,2,'72655883','CRISTIAN MESTANZA ORTIZ','-',1,1),(221,2,'-','CLiente varios','-',1,1),(222,2,'-','CLiente varios','-',1,1),(223,2,'-','CLiente varios','-',1,1),(224,2,'72655883','CRISTIAN MESTANZA ORTIZ','-',1,1),(225,2,'72655883','CRISTIAN MESTANZA ORTIZ','-',1,1),(226,2,'72655883','CRISTIAN MESTANZA ORTIZ','-',1,1),(227,1,'-','CLiente varios','-',1,2),(228,2,'-','CLiente varios','-',1,1),(229,2,'-','CLiente varios','-',1,1),(230,2,'-','CLiente varios','-',1,1),(231,2,'-','CLiente varios','-',1,1);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `codigo_correo`
--

DROP TABLE IF EXISTS `codigo_correo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `codigo_correo` (
  `id_codigo_correo` int NOT NULL AUTO_INCREMENT,
  `codigo` varchar(45) DEFAULT NULL,
  `correo` varchar(80) DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_codigo_correo`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codigo_correo`
--

LOCK TABLES `codigo_correo` WRITE;
/*!40000 ALTER TABLE `codigo_correo` DISABLE KEYS */;
/*!40000 ALTER TABLE `codigo_correo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra_detalle`
--

DROP TABLE IF EXISTS `compra_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra_detalle` (
  `idcompradetalle` int NOT NULL AUTO_INCREMENT,
  `idcompra` int NOT NULL,
  `idproducto` int NOT NULL,
  `cantidad` int NOT NULL,
  `subtotal` double NOT NULL,
  PRIMARY KEY (`idcompradetalle`),
  KEY `fk_producto_compra_detalle` (`idproducto`),
  KEY `fk_compra_compra_detalle` (`idcompra`),
  CONSTRAINT `fk_compra_compra_detalle` FOREIGN KEY (`idcompra`) REFERENCES `compras` (`idcompra`),
  CONSTRAINT `fk_producto_compra_detalle` FOREIGN KEY (`idproducto`) REFERENCES `producto` (`idproducto`)
) ENGINE=InnoDB AUTO_INCREMENT=166 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra_detalle`
--

LOCK TABLES `compra_detalle` WRITE;
/*!40000 ALTER TABLE `compra_detalle` DISABLE KEYS */;
INSERT INTO `compra_detalle` VALUES (158,471,368,2,6),(159,472,369,2,4),(160,473,369,2,4),(161,473,368,3,9),(162,474,369,2,4),(163,475,369,3,6),(164,476,370,1,2),(165,477,371,3,6);
/*!40000 ALTER TABLE `compra_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compras`
--

DROP TABLE IF EXISTS `compras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compras` (
  `idcompra` int NOT NULL AUTO_INCREMENT,
  `idproveedor` int NOT NULL,
  `numcorrelativo` varchar(50) DEFAULT NULL,
  `fechacompra` date DEFAULT NULL,
  `estado` int DEFAULT '1',
  `idsucursal` int DEFAULT NULL,
  PRIMARY KEY (`idcompra`),
  KEY `fk_compra_proveedores` (`idproveedor`),
  KEY `fk_compras_sucursal_idx` (`idsucursal`),
  CONSTRAINT `fk_compra_proveedores` FOREIGN KEY (`idproveedor`) REFERENCES `proveedores` (`idproveedor`),
  CONSTRAINT `fk_compras_sucursal` FOREIGN KEY (`idsucursal`) REFERENCES `sucursal` (`idsucursal`)
) ENGINE=InnoDB AUTO_INCREMENT=478 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compras`
--

LOCK TABLES `compras` WRITE;
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
INSERT INTO `compras` VALUES (471,4,'B001-0001','2026-05-29',0,NULL),(472,4,'F001-0001','2026-05-29',0,NULL),(473,4,'F001-0001','2026-05-29',1,NULL),(474,4,'F0002-0001','2026-05-29',1,NULL),(475,4,'B001-003','2026-05-30',1,NULL),(476,4,'B004-001','2026-06-04',1,2),(477,4,'B002 - 005','2026-06-04',1,1);
/*!40000 ALTER TABLE `compras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion`
--

DROP TABLE IF EXISTS `cotizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cotizacion` (
  `idcotizacion` int NOT NULL AUTO_INCREMENT,
  `idcliente` int NOT NULL,
  `fecha` date NOT NULL,
  `total` double DEFAULT '0',
  `observaciones` varchar(500) DEFAULT NULL,
  `estado` int DEFAULT '1',
  PRIMARY KEY (`idcotizacion`),
  KEY `idcliente` (`idcliente`),
  CONSTRAINT `cotizacion_ibfk_1` FOREIGN KEY (`idcliente`) REFERENCES `clientes` (`idcliente`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion`
--

LOCK TABLES `cotizacion` WRITE;
/*!40000 ALTER TABLE `cotizacion` DISABLE KEYS */;
INSERT INTO `cotizacion` VALUES (1,220,'2026-06-03',14,'',1);
/*!40000 ALTER TABLE `cotizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_detalle`
--

DROP TABLE IF EXISTS `cotizacion_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cotizacion_detalle` (
  `idcotizaciondetalle` int NOT NULL AUTO_INCREMENT,
  `idcotizacion` int NOT NULL,
  `producto` varchar(255) NOT NULL,
  `descripcion` varchar(500) DEFAULT NULL,
  `cantidad` double NOT NULL,
  `preciounitario` double NOT NULL,
  `subtotal` double NOT NULL,
  PRIMARY KEY (`idcotizaciondetalle`),
  KEY `idcotizacion` (`idcotizacion`),
  CONSTRAINT `cotizacion_detalle_ibfk_1` FOREIGN KEY (`idcotizacion`) REFERENCES `cotizacion` (`idcotizacion`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_detalle`
--

LOCK TABLES `cotizacion_detalle` WRITE;
/*!40000 ALTER TABLE `cotizacion_detalle` DISABLE KEYS */;
INSERT INTO `cotizacion_detalle` VALUES (1,1,'Yogur','',4,2,8),(2,1,'Gaseosa','',3,2,6);
/*!40000 ALTER TABLE `cotizacion_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cuenta_bancaria`
--

DROP TABLE IF EXISTS `cuenta_bancaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cuenta_bancaria` (
  `idcuentabancaria` int NOT NULL AUTO_INCREMENT,
  `idcliente` int NOT NULL,
  `banco` varchar(50) NOT NULL,
  `numero_cuenta` varchar(50) NOT NULL,
  `tipo_cuenta` varchar(20) DEFAULT 'Ahorro',
  `estado` int DEFAULT '1',
  PRIMARY KEY (`idcuentabancaria`),
  KEY `idcliente` (`idcliente`),
  CONSTRAINT `cuenta_bancaria_ibfk_1` FOREIGN KEY (`idcliente`) REFERENCES `clientes` (`idcliente`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cuenta_bancaria`
--

LOCK TABLES `cuenta_bancaria` WRITE;
/*!40000 ALTER TABLE `cuenta_bancaria` DISABLE KEYS */;
INSERT INTO `cuenta_bancaria` VALUES (1,220,'BCP','123123','Corriente',1);
/*!40000 ALTER TABLE `cuenta_bancaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departamentos`
--

DROP TABLE IF EXISTS `departamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamentos` (
  `iddepartamentos` varchar(11) NOT NULL,
  `nombredepartamento` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`iddepartamentos`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamentos`
--

LOCK TABLES `departamentos` WRITE;
/*!40000 ALTER TABLE `departamentos` DISABLE KEYS */;
INSERT INTO `departamentos` VALUES ('01','Amazonas'),('02','Ancash'),('03','Apurimac'),('04','Arequipa'),('05','Ayacucho'),('06','Cajamarca'),('07','Callao'),('08','Cusco'),('09','Huancavelica'),('10','Huanuco'),('11','Ica'),('12','Junin'),('13','La Libertad'),('14','Lambayeque'),('15','Lima'),('16','Loreto'),('17','Madre de Dios'),('18','Moquegua'),('19','Pasco'),('20','Piura'),('21','Puno'),('22','San Martin'),('23','Tacna'),('24','Tumbes'),('25','Ucayali');
/*!40000 ALTER TABLE `departamentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detallecategoriaxunidades`
--

DROP TABLE IF EXISTS `detallecategoriaxunidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detallecategoriaxunidades` (
  `iddetallecategoriaxunidades` int NOT NULL AUTO_INCREMENT,
  `idcategoria` int NOT NULL,
  `idunidad` int NOT NULL,
  PRIMARY KEY (`iddetallecategoriaxunidades`),
  KEY `idcategoria` (`idcategoria`),
  KEY `idunidad` (`idunidad`),
  CONSTRAINT `detallecategoriaxunidades_ibfk_1` FOREIGN KEY (`idcategoria`) REFERENCES `categoria` (`idcategoria`),
  CONSTRAINT `detallecategoriaxunidades_ibfk_2` FOREIGN KEY (`idunidad`) REFERENCES `unidades` (`idunidad`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detallecategoriaxunidades`
--

LOCK TABLES `detallecategoriaxunidades` WRITE;
/*!40000 ALTER TABLE `detallecategoriaxunidades` DISABLE KEYS */;
/*!40000 ALTER TABLE `detallecategoriaxunidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalletipoigvxdepartamento`
--

DROP TABLE IF EXISTS `detalletipoigvxdepartamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalletipoigvxdepartamento` (
  `iddetalletipoigvxdepartamento` int NOT NULL AUTO_INCREMENT,
  `id_tipo_igv` int NOT NULL,
  `iddepartamentos` varchar(11) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL COMMENT '	',
  PRIMARY KEY (`iddetalletipoigvxdepartamento`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalletipoigvxdepartamento`
--

LOCK TABLES `detalletipoigvxdepartamento` WRITE;
/*!40000 ALTER TABLE `detalletipoigvxdepartamento` DISABLE KEYS */;
INSERT INTO `detalletipoigvxdepartamento` VALUES (2,9,'01'),(3,1,'02'),(4,1,'03'),(5,1,'04'),(6,1,'05'),(7,1,'06'),(8,1,'07'),(9,1,'08'),(10,1,'09'),(11,1,'10'),(12,1,'11'),(13,1,'12'),(14,1,'13'),(15,1,'14'),(16,1,'15'),(17,9,'16'),(18,9,'17'),(19,1,'18'),(20,1,'19'),(21,1,'20'),(22,1,'21'),(23,9,'22'),(24,1,'23'),(25,1,'24'),(26,9,'25');
/*!40000 ALTER TABLE `detalletipoigvxdepartamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalletipousuarioxmodulos`
--

DROP TABLE IF EXISTS `detalletipousuarioxmodulos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalletipousuarioxmodulos` (
  `iddetalletipousuarioxmodulos` int NOT NULL AUTO_INCREMENT,
  `idtipousuario` int NOT NULL,
  `idmodulo` int NOT NULL,
  PRIMARY KEY (`iddetalletipousuarioxmodulos`),
  KEY `idmodulo` (`idmodulo`),
  KEY `idtipousuario` (`idtipousuario`),
  CONSTRAINT `detalletipousuarioxmodulos_ibfk_1` FOREIGN KEY (`idmodulo`) REFERENCES `modulos` (`idmodulo`),
  CONSTRAINT `detalletipousuarioxmodulos_ibfk_2` FOREIGN KEY (`idtipousuario`) REFERENCES `tipousuario` (`idtipousuario`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalletipousuarioxmodulos`
--

LOCK TABLES `detalletipousuarioxmodulos` WRITE;
/*!40000 ALTER TABLE `detalletipousuarioxmodulos` DISABLE KEYS */;
INSERT INTO `detalletipousuarioxmodulos` VALUES (1,1,1),(2,1,2),(3,1,3),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(11,1,12),(19,1,13),(20,1,14),(21,1,15),(25,1,16),(26,10,1),(27,10,2),(28,10,16),(29,1,17),(30,1,18),(31,1,19),(33,10,19),(74,3,7),(75,3,8),(76,3,12),(77,3,13),(78,3,20),(79,2,1),(80,2,2),(81,2,3),(82,2,5),(83,2,6),(84,2,7),(85,2,16),(86,2,17),(87,2,18),(88,2,19),(89,2,23);
/*!40000 ALTER TABLE `detalletipousuarioxmodulos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `distritos`
--

DROP TABLE IF EXISTS `distritos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `distritos` (
  `iddistrito` varchar(11) NOT NULL,
  `nombredistrito` varchar(255) NOT NULL,
  `idprovincia` varchar(11) NOT NULL,
  `ubigeo` varchar(255) DEFAULT NULL,
  `checked` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`iddistrito`),
  KEY `fk_provincia_distritos` (`idprovincia`),
  CONSTRAINT `fk_provincia_distritos` FOREIGN KEY (`idprovincia`) REFERENCES `provincias` (`idprovincia`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `distritos`
--

LOCK TABLES `distritos` WRITE;
/*!40000 ALTER TABLE `distritos` DISABLE KEYS */;
INSERT INTO `distritos` VALUES ('010101','Chachapoyas','0101','010101',1),('010102','Asuncion','0101','010102',1),('010103','Balsas','0101','010103',1),('010104','Cheto','0101','010104',1),('010105','Chiliquin','0101','010105',1),('010106','Chuquibamba','0101','010106',1),('010107','Granada','0101','010107',1),('010108','Huancas','0101','010108',1),('010109','La Jalca','0101','010109',1),('010110','Leimebamba','0101','010110',1),('010111','Levanto','0101','010111',1),('010112','Magdalena','0101','010112',1),('010113','Mariscal Castilla','0101','010113',1),('010114','Molinopampa','0101','010114',1),('010115','Montevideo','0101','010115',1),('010116','Olleros','0101','010116',1),('010117','Quinjalca','0101','010117',1),('010118','San Francisco de Daguas','0101','010118',1),('010119','San Isidro de Maino','0101','010119',1),('010120','Soloco','0101','010120',1),('010121','Sonche','0101','010121',1),('010201','Bagua','0102','010201',1),('010202','Aramango','0102','010202',1),('010203','Copallin','0102','010203',1),('010204','El Parco','0102','010204',1),('010205','Imaza','0102','010205',1),('010206','La Peca','0102','010206',1),('010301','Jumbilla','0103','010301',1),('010302','Chisquilla','0103','010302',1),('010303','Churuja','0103','010303',1),('010304','Corosha','0103','010304',1),('010305','Cuispes','0103','010305',1),('010306','Florida','0103','010306',1),('010307','Jazan','0103','010307',1),('010308','Recta','0103','010308',1),('010309','San Carlos','0103','010309',1),('010310','Shipasbamba','0103','010310',1),('010311','Valera','0103','010311',1),('010312','Yambrasbamba','0103','010312',1),('010401','Nieva','0104','010401',1),('010402','El Cenepa','0104','010402',1),('010403','Rio Santiago','0104','010403',1),('010501','Lamud','0105','010501',1),('010502','Camporredondo','0105','010502',1),('010503','Cocabamba','0105','010503',1),('010504','Colcamar','0105','010504',1),('010505','Conila','0105','010505',1),('010506','Inguilpata','0105','010506',1),('010507','Longuita','0105','010507',1),('010508','Lonya Chico','0105','010508',1),('010509','Luya','0105','010509',1),('010510','Luya Viejo','0105','010510',1),('010511','Maria','0105','010511',1),('010512','Ocalli','0105','010512',1),('010513','Ocumal','0105','010513',1),('010514','Pisuquia','0105','010514',1),('010515','Providencia','0105','010515',1),('010516','San Cristobal','0105','010516',1),('010517','San Francisco del Yeso','0105','010517',1),('010518','San Jeronimo','0105','010518',1),('010519','San Juan de Lopecancha','0105','010519',1),('010520','Santa Catalina','0105','010520',1),('010521','Santo Tomas','0105','010521',1),('010522','Tingo','0105','010522',1),('010523','Trita','0105','010523',1),('010601','San Nicolas','0106','010601',1),('010602','Chirimoto','0106','010602',1),('010603','Cochamal','0106','010603',1),('010604','Huambo','0106','010604',1),('010605','Limabamba','0106','010605',1),('010606','Longar','0106','010606',1),('010607','Mariscal Benavides','0106','010607',1),('010608','Milpuc','0106','010608',1),('010609','Omia','0106','010609',1),('010610','Santa Rosa','0106','010610',1),('010611','Totora','0106','010611',1),('010612','Vista Alegre','0106','010612',1),('010701','Bagua Grande','0107','010701',1),('010702','Cajaruro','0107','010702',1),('010703','Cumba','0107','010703',1),('010704','El Milagro','0107','010704',1),('010705','Jamalca','0107','010705',1),('010706','Lonya Grande','0107','010706',1),('010707','Yamon','0107','010707',1),('020101','Huaraz','0201','020101',1),('020102','Cochabamba','0201','020102',1),('020103','Colcabamba','0201','020103',1),('020104','Huanchay','0201','020104',1),('020105','Independencia','0201','020105',1),('020106','Jangas','0201','020106',1),('020107','La Libertad','0201','020107',1),('020108','Olleros','0201','020108',1),('020109','Pampas','0201','020109',1),('020110','Pariacoto','0201','020110',1),('020111','Pira','0201','020111',1),('020112','Tarica','0201','020112',1),('020201','Aija','0202','020201',1),('020202','Coris','0202','020202',1),('020203','Huacllan','0202','020203',1),('020204','La Merced','0202','020204',1),('020205','Succha','0202','020205',1),('020301','Llamellin','0203','020301',1),('020302','Aczo','0203','020302',1),('020303','Chaccho','0203','020303',1),('020304','Chingas','0203','020304',1),('020305','Mirgas','0203','020305',1),('020306','San Juan de Rontoy','0203','020306',1),('020401','Chacas','0204','020401',1),('020402','Acochaca','0204','020402',1),('020501','Chiquian','0205','020501',1),('020502','Abelardo Pardo Lezameta','0205','020502',1),('020503','Antonio Raymondi','0205','020503',1),('020504','Aquia','0205','020504',1),('020505','Cajacay','0205','020505',1),('020506','Canis','0205','020506',1),('020507','Colquioc','0205','020507',1),('020508','Huallanca','0205','020508',1),('020509','Huasta','0205','020509',1),('020510','Huayllacayan','0205','020510',1),('020511','La Primavera','0205','020511',1),('020512','Mangas','0205','020512',1),('020513','Pacllon','0205','020513',1),('020514','San Miguel de Corpanqui','0205','020514',1),('020515','Ticllos','0205','020515',1),('020601','Carhuaz','0206','020601',1),('020602','Acopampa','0206','020602',1),('020603','Amashca','0206','020603',1),('020604','Anta','0206','020604',1),('020605','Ataquero','0206','020605',1),('020606','Marcara','0206','020606',1),('020607','Pariahuanca','0206','020607',1),('020608','San Miguel de Aco','0206','020608',1),('020609','Shilla','0206','020609',1),('020610','Tinco','0206','020610',1),('020611','Yungar','0206','020611',1),('020701','San Luis','0207','020701',1),('020702','San Nicolas','0207','020702',1),('020703','Yauya','0207','020703',1),('020801','Casma','0208','020801',1),('020802','Buena Vista Alta','0208','020802',1),('020803','Comandante Noel','0208','020803',1),('020804','Yautan','0208','020804',1),('020901','Corongo','0209','020901',1),('020902','Aco','0209','020902',1),('020903','Bambas','0209','020903',1),('020904','Cusca','0209','020904',1),('020905','La Pampa','0209','020905',1),('020906','Yanac','0209','020906',1),('020907','Yupan','0209','020907',1),('021001','Huari','0210','021001',1),('021002','Anra','0210','021002',1),('021003','Cajay','0210','021003',1),('021004','Chavin de Huantar','0210','021004',1),('021005','Huacachi','0210','021005',1),('021006','Huacchis','0210','021006',1),('021007','Huachis','0210','021007',1),('021008','Huantar','0210','021008',1),('021009','Masin','0210','021009',1),('021010','Paucas','0210','021010',1),('021011','Ponto','0210','021011',1),('021012','Rahuapampa','0210','021012',1),('021013','Rapayan','0210','021013',1),('021014','San Marcos','0210','021014',1),('021015','San Pedro de Chana','0210','021015',1),('021016','Uco','0210','021016',1),('021101','Huarmey','0211','021101',1),('021102','Cochapeti','0211','021102',1),('021103','Culebras','0211','021103',1),('021104','Huayan','0211','021104',1),('021105','Malvas','0211','021105',1),('021201','Caraz','0212','021201',1),('021202','Huallanca','0212','021202',1),('021203','Huata','0212','021203',1),('021204','Huaylas','0212','021204',1),('021205','Mato','0212','021205',1),('021206','Pamparomas','0212','021206',1),('021207','Pueblo Libre','0212','021207',1),('021208','Santa Cruz','0212','021208',1),('021209','Santo Toribio','0212','021209',1),('021210','Yuracmarca','0212','021210',1),('021301','Piscobamba','0213','021301',1),('021302','Casca','0213','021302',1),('021303','Eleazar Guzman Barron','0213','021303',1),('021304','Fidel Olivas Escudero','0213','021304',1),('021305','Llama','0213','021305',1),('021306','Llumpa','0213','021306',1),('021307','Lucma','0213','021307',1),('021308','Musga','0213','021308',1),('021401','Ocros','0214','021401',1),('021402','Acas','0214','021402',1),('021403','Cajamarquilla','0214','021403',1),('021404','Carhuapampa','0214','021404',1),('021405','Cochas','0214','021405',1),('021406','Congas','0214','021406',1),('021407','Llipa','0214','021407',1),('021408','San Cristobal de Rajan','0214','021408',1),('021409','San Pedro','0214','021409',1),('021410','Santiago de Chilcas','0214','021410',1),('021501','Cabana','0215','021501',1),('021502','Bolognesi','0215','021502',1),('021503','Conchucos','0215','021503',1),('021504','Huacaschuque','0215','021504',1),('021505','Huandoval','0215','021505',1),('021506','Lacabamba','0215','021506',1),('021507','Llapo','0215','021507',1),('021508','Pallasca','0215','021508',1),('021509','Pampas','0215','021509',1),('021510','Santa Rosa','0215','021510',1),('021511','Tauca','0215','021511',1),('021601','Pomabamba','0216','021601',1),('021602','Huayllan','0216','021602',1),('021603','Parobamba','0216','021603',1),('021604','Quinuabamba','0216','021604',1),('021701','Recuay','0217','021701',1),('021702','Catac','0217','021702',1),('021703','Cotaparaco','0217','021703',1),('021704','Huayllapampa','0217','021704',1),('021705','Llacllin','0217','021705',1),('021706','Marca','0217','021706',1),('021707','Pampas Chico','0217','021707',1),('021708','Pararin','0217','021708',1),('021709','Tapacocha','0217','021709',1),('021710','Ticapampa','0217','021710',1),('021801','Chimbote','0218','021801',1),('021802','Caceres del Peru','0218','021802',1),('021803','Coishco','0218','021803',1),('021804','Macate','0218','021804',1),('021805','Moro','0218','021805',1),('021806','Nepeña','0218','021806',1),('021807','Samanco','0218','021807',1),('021808','Santa','0218','021808',1),('021809','Nuevo Chimbote','0218','021809',1),('021901','Sihuas','0219','021901',1),('021902','Acobamba','0219','021902',1),('021903','Alfonso Ugarte','0219','021903',1),('021904','Cashapampa','0219','021904',1),('021905','Chingalpo','0219','021905',1),('021906','Huayllabamba','0219','021906',1),('021907','Quiches','0219','021907',1),('021908','Ragash','0219','021908',1),('021909','San Juan','0219','021909',1),('021910','Sicsibamba','0219','021910',1),('022001','Yungay','0220','022001',1),('022002','Cascapara','0220','022002',1),('022003','Mancos','0220','022003',1),('022004','Matacoto','0220','022004',1),('022005','Quillo','0220','022005',1),('022006','Ranrahirca','0220','022006',1),('022007','Shupluy','0220','022007',1),('022008','Yanama','0220','022008',1),('030101','Abancay','0301','030101',1),('030102','Chacoche','0301','030102',1),('030103','Circa','0301','030103',1),('030104','Curahuasi','0301','030104',1),('030105','Huanipaca','0301','030105',1),('030106','Lambrama','0301','030106',1),('030107','Pichirhua','0301','030107',1),('030108','San Pedro de Cachora','0301','030108',1),('030109','Tamburco','0301','030109',1),('030201','Andahuaylas','0302','030201',1),('030202','Andarapa','0302','030202',1),('030203','Chiara','0302','030203',1),('030204','Huancarama','0302','030204',1),('030205','Huancaray','0302','030205',1),('030206','Huayana','0302','030206',1),('030207','Kishuara','0302','030207',1),('030208','Pacobamba','0302','030208',1),('030209','Pacucha','0302','030209',1),('030210','Pampachiri','0302','030210',1),('030211','Pomacocha','0302','030211',1),('030212','San Antonio de Cachi','0302','030212',1),('030213','San Jeronimo','0302','030213',1),('030214','San Miguel de Chaccrampa','0302','030214',1),('030215','Santa Maria de Chicmo','0302','030215',1),('030216','Talavera','0302','030216',1),('030217','Tumay Huaraca','0302','030217',1),('030218','Turpo','0302','030218',1),('030219','Kaquiabamba','0302','030219',1),('030220','José María Arguedas','0302','030220',1),('030301','Antabamba','0303','030301',1),('030302','El Oro','0303','030302',1),('030303','Huaquirca','0303','030303',1),('030304','Juan Espinoza Medrano','0303','030304',1),('030305','Oropesa','0303','030305',1),('030306','Pachaconas','0303','030306',1),('030307','Sabaino','0303','030307',1),('030401','Chalhuanca','0304','030401',1),('030402','Capaya','0304','030402',1),('030403','Caraybamba','0304','030403',1),('030404','Chapimarca','0304','030404',1),('030405','Colcabamba','0304','030405',1),('030406','Cotaruse','0304','030406',1),('030407','Huayllo','0304','030407',1),('030408','Justo Apu Sahuaraura','0304','030408',1),('030409','Lucre','0304','030409',1),('030410','Pocohuanca','0304','030410',1),('030411','San Juan de Chacña','0304','030411',1),('030412','Sañayca','0304','030412',1),('030413','Soraya','0304','030413',1),('030414','Tapairihua','0304','030414',1),('030415','Tintay','0304','030415',1),('030416','Toraya','0304','030416',1),('030417','Yanaca','0304','030417',1),('030501','Tambobamba','0305','030501',1),('030502','Cotabambas','0305','030502',1),('030503','Coyllurqui','0305','030503',1),('030504','Haquira','0305','030504',1),('030505','Mara','0305','030505',1),('030506','Challhuahuacho','0305','030506',1),('030601','Chincheros','0306','030601',1),('030602','Anco_Huallo','0306','030602',1),('030603','Cocharcas','0306','030603',1),('030604','Huaccana','0306','030604',1),('030605','Ocobamba','0306','030605',1),('030606','Ongoy','0306','030606',1),('030607','Uranmarca','0306','030607',1),('030608','Ranracancha','0306','030608',1),('030609','Rocchacc','0306','030609',1),('030610','El Porvenir','0306','030610',1),('030611','Los Chankas','0306','030611',1),('030701','Chuquibambilla','0307','030701',1),('030702','Curpahuasi','0307','030702',1),('030703','Gamarra','0307','030703',1),('030704','Huayllati','0307','030704',1),('030705','Mamara','0307','030705',1),('030706','Micaela Bastidas','0307','030706',1),('030707','Pataypampa','0307','030707',1),('030708','Progreso','0307','030708',1),('030709','San Antonio','0307','030709',1),('030710','Santa Rosa','0307','030710',1),('030711','Turpay','0307','030711',1),('030712','Vilcabamba','0307','030712',1),('030713','Virundo','0307','030713',1),('030714','Curasco','0307','030714',1),('040101','Arequipa','0401','040101',1),('040102','Alto Selva Alegre','0401','040102',1),('040103','Cayma','0401','040103',1),('040104','Cerro Colorado','0401','040104',1),('040105','Characato','0401','040105',1),('040106','Chiguata','0401','040106',1),('040107','Jacobo Hunter','0401','040107',1),('040108','La Joya','0401','040108',1),('040109','Mariano Melgar','0401','040109',1),('040110','Miraflores','0401','040110',1),('040111','Mollebaya','0401','040111',1),('040112','Paucarpata','0401','040112',1),('040113','Pocsi','0401','040113',1),('040114','Polobaya','0401','040114',1),('040115','Quequeña','0401','040115',1),('040116','Sabandia','0401','040116',1),('040117','Sachaca','0401','040117',1),('040118','San Juan de Siguas','0401','040118',1),('040119','San Juan de Tarucani','0401','040119',1),('040120','Santa Isabel de Siguas','0401','040120',1),('040121','Santa Rita de Siguas','0401','040121',1),('040122','Socabaya','0401','040122',1),('040123','Tiabaya','0401','040123',1),('040124','Uchumayo','0401','040124',1),('040125','Vitor','0401','040125',1),('040126','Yanahuara','0401','040126',1),('040127','Yarabamba','0401','040127',1),('040128','Yura','0401','040128',1),('040129','Jose Luis Bustamante y Rivero','0401','040129',1),('040201','Camana','0402','040201',1),('040202','Jose Maria Quimper','0402','040202',1),('040203','Mariano Nicolas Valcarcel','0402','040203',1),('040204','Mariscal Caceres','0402','040204',1),('040205','Nicolas de Pierola','0402','040205',1),('040206','Ocoña','0402','040206',1),('040207','Quilca','0402','040207',1),('040208','Samuel Pastor','0402','040208',1),('040301','Caraveli','0403','040301',1),('040302','Acari','0403','040302',1),('040303','Atico','0403','040303',1),('040304','Atiquipa','0403','040304',1),('040305','Bella Union','0403','040305',1),('040306','Cahuacho','0403','040306',1),('040307','Chala','0403','040307',1),('040308','Chaparra','0403','040308',1),('040309','Huanuhuanu','0403','040309',1),('040310','Jaqui','0403','040310',1),('040311','Lomas','0403','040311',1),('040312','Quicacha','0403','040312',1),('040313','Yauca','0403','040313',1),('040401','Aplao','0404','040401',1),('040402','Andagua','0404','040402',1),('040403','Ayo','0404','040403',1),('040404','Chachas','0404','040404',1),('040405','Chilcaymarca','0404','040405',1),('040406','Choco','0404','040406',1),('040407','Huancarqui','0404','040407',1),('040408','Machaguay','0404','040408',1),('040409','Orcopampa','0404','040409',1),('040410','Pampacolca','0404','040410',1),('040411','Tipan','0404','040411',1),('040412','Uñon','0404','040412',1),('040413','Uraca','0404','040413',1),('040414','Viraco','0404','040414',1),('040501','Chivay','0405','040501',1),('040502','Achoma','0405','040502',1),('040503','Cabanaconde','0405','040503',1),('040504','Callalli','0405','040504',1),('040505','Caylloma','0405','040505',1),('040506','Coporaque','0405','040506',1),('040507','Huambo','0405','040507',1),('040508','Huanca','0405','040508',1),('040509','Ichupampa','0405','040509',1),('040510','Lari','0405','040510',1),('040511','Lluta','0405','040511',1),('040512','Maca','0405','040512',1),('040513','Madrigal','0405','040513',1),('040514','San Antonio de Chuca','0405','040514',1),('040515','Sibayo','0405','040515',1),('040516','Tapay','0405','040516',1),('040517','Tisco','0405','040517',1),('040518','Tuti','0405','040518',1),('040519','Yanque','0405','040519',1),('040520','Majes','0405','040520',1),('040601','Chuquibamba','0406','040601',1),('040602','Andaray','0406','040602',1),('040603','Cayarani','0406','040603',1),('040604','Chichas','0406','040604',1),('040605','Iray','0406','040605',1),('040606','Rio Grande','0406','040606',1),('040607','Salamanca','0406','040607',1),('040608','Yanaquihua','0406','040608',1),('040701','Mollendo','0407','040701',1),('040702','Cocachacra','0407','040702',1),('040703','Dean Valdivia','0407','040703',1),('040704','Islay','0407','040704',1),('040705','Mejia','0407','040705',1),('040706','Punta de Bombon','0407','040706',1),('040801','Cotahuasi','0408','040801',1),('040802','Alca','0408','040802',1),('040803','Charcana','0408','040803',1),('040804','Huaynacotas','0408','040804',1),('040805','Pampamarca','0408','040805',1),('040806','Puyca','0408','040806',1),('040807','Quechualla','0408','040807',1),('040808','Sayla','0408','040808',1),('040809','Tauria','0408','040809',1),('040810','Tomepampa','0408','040810',1),('040811','Toro','0408','040811',1),('050101','Ayacucho','0501','050101',1),('050102','Acocro','0501','050102',1),('050103','Acos Vinchos','0501','050103',1),('050104','Carmen Alto','0501','050104',1),('050105','Chiara','0501','050105',1),('050106','Ocros','0501','050106',1),('050107','Pacaycasa','0501','050107',1),('050108','Quinua','0501','050108',1),('050109','San Jose de Ticllas','0501','050109',1),('050110','San Juan Bautista','0501','050110',1),('050111','Santiago de Pischa','0501','050111',1),('050112','Socos','0501','050112',1),('050113','Tambillo','0501','050113',1),('050114','Vinchos','0501','050114',1),('050115','Jesus Nazareno','0501','050115',1),('050116','Andrés Avelino Cáceres Dorregaray','0501','050116',1),('050201','Cangallo','0502','050201',1),('050202','Chuschi','0502','050202',1),('050203','Los Morochucos','0502','050203',1),('050204','Maria Parado de Bellido','0502','050204',1),('050205','Paras','0502','050205',1),('050206','Totos','0502','050206',1),('050301','Sancos','0503','050301',1),('050302','Carapo','0503','050302',1),('050303','Sacsamarca','0503','050303',1),('050304','Santiago de Lucanamarca','0503','050304',1),('050401','Huanta','0504','050401',1),('050402','Ayahuanco','0504','050402',1),('050403','Huamanguilla','0504','050403',1),('050404','Iguain','0504','050404',1),('050405','Luricocha','0504','050405',1),('050406','Santillana','0504','050406',1),('050407','Sivia','0504','050407',1),('050408','Llochegua','0504','050408',1),('050409','Canayre','0504','050409',1),('050410','Uchuraccay','0504','050410',1),('050411','Pucacolpa','0504','050411',1),('050412','Chaca','0504','050412',1),('050501','San Miguel','0505','050501',1),('050502','Anco','0505','050502',1),('050503','Ayna','0505','050503',1),('050504','Chilcas','0505','050504',1),('050505','Chungui','0505','050505',1),('050506','Luis Carranza','0505','050506',1),('050507','Santa Rosa','0505','050507',1),('050508','Tambo','0505','050508',1),('050509','Samugari','0505','050509',1),('050510','Anchihuay','0505','050510',1),('050511','Oronccoy','0505','050511',1),('050601','Puquio','0506','050601',1),('050602','Aucara','0506','050602',1),('050603','Cabana','0506','050603',1),('050604','Carmen Salcedo','0506','050604',1),('050605','Chaviña','0506','050605',1),('050606','Chipao','0506','050606',1),('050607','Huac-Huas','0506','050607',1),('050608','Laramate','0506','050608',1),('050609','Leoncio Prado','0506','050609',1),('050610','Llauta','0506','050610',1),('050611','Lucanas','0506','050611',1),('050612','Ocaña','0506','050612',1),('050613','Otoca','0506','050613',1),('050614','Saisa','0506','050614',1),('050615','San Cristobal','0506','050615',1),('050616','San Juan','0506','050616',1),('050617','San Pedro','0506','050617',1),('050618','San Pedro de Palco','0506','050618',1),('050619','Sancos','0506','050619',1),('050620','Santa Ana de Huaycahuacho','0506','050620',1),('050621','Santa Lucia','0506','050621',1),('050701','Coracora','0507','050701',1),('050702','Chumpi','0507','050702',1),('050703','Coronel Castañeda','0507','050703',1),('050704','Pacapausa','0507','050704',1),('050705','Pullo','0507','050705',1),('050706','Puyusca','0507','050706',1),('050707','San Francisco de Ravacayco','0507','050707',1),('050708','Upahuacho','0507','050708',1),('050801','Pausa','0508','050801',1),('050802','Colta','0508','050802',1),('050803','Corculla','0508','050803',1),('050804','Lampa','0508','050804',1),('050805','Marcabamba','0508','050805',1),('050806','Oyolo','0508','050806',1),('050807','Pararca','0508','050807',1),('050808','San Javier de Alpabamba','0508','050808',1),('050809','San Jose de Ushua','0508','050809',1),('050810','Sara Sara','0508','050810',1),('050901','Querobamba','0509','050901',1),('050902','Belen','0509','050902',1),('050903','Chalcos','0509','050903',1),('050904','Chilcayoc','0509','050904',1),('050905','Huacaña','0509','050905',1),('050906','Morcolla','0509','050906',1),('050907','Paico','0509','050907',1),('050908','San Pedro de Larcay','0509','050908',1),('050909','San Salvador de Quije','0509','050909',1),('050910','Santiago de Paucaray','0509','050910',1),('050911','Soras','0509','050911',1),('051001','Huancapi','0510','051001',1),('051002','Alcamenca','0510','051002',1),('051003','Apongo','0510','051003',1),('051004','Asquipata','0510','051004',1),('051005','Canaria','0510','051005',1),('051006','Cayara','0510','051006',1),('051007','Colca','0510','051007',1),('051008','Huamanquiquia','0510','051008',1),('051009','Huancaraylla','0510','051009',1),('051010','Huaya','0510','051010',1),('051011','Sarhua','0510','051011',1),('051012','Vilcanchos','0510','051012',1),('051101','Vilcas Huaman','0511','051101',1),('051102','Accomarca','0511','051102',1),('051103','Carhuanca','0511','051103',1),('051104','Concepcion','0511','051104',1),('051105','Huambalpa','0511','051105',1),('051106','Independencia','0511','051106',1),('051107','Saurama','0511','051107',1),('051108','Vischongo','0511','051108',1),('060101','Cajamarca','0601','060101',1),('060102','Asuncion','0601','060102',1),('060103','Chetilla','0601','060103',1),('060104','Cospan','0601','060104',1),('060105','Encañada','0601','060105',1),('060106','Jesus','0601','060106',1),('060107','Llacanora','0601','060107',1),('060108','Los Baños del Inca','0601','060108',1),('060109','Magdalena','0601','060109',1),('060110','Matara','0601','060110',1),('060111','Namora','0601','060111',1),('060112','San Juan','0601','060112',1),('060201','Cajabamba','0602','060201',1),('060202','Cachachi','0602','060202',1),('060203','Condebamba','0602','060203',1),('060204','Sitacocha','0602','060204',1),('060301','Celendin','0603','060301',1),('060302','Chumuch','0603','060302',1),('060303','Cortegana','0603','060303',1),('060304','Huasmin','0603','060304',1),('060305','Jorge Chavez','0603','060305',1),('060306','Jose Galvez','0603','060306',1),('060307','Miguel Iglesias','0603','060307',1),('060308','Oxamarca','0603','060308',1),('060309','Sorochuco','0603','060309',1),('060310','Sucre','0603','060310',1),('060311','Utco','0603','060311',1),('060312','La Libertad de Pallan','0603','060312',1),('060401','Chota','0604','060401',1),('060402','Anguia','0604','060402',1),('060403','Chadin','0604','060403',1),('060404','Chiguirip','0604','060404',1),('060405','Chimban','0604','060405',1),('060406','Choropampa','0604','060406',1),('060407','Cochabamba','0604','060407',1),('060408','Conchan','0604','060408',1),('060409','Huambos','0604','060409',1),('060410','Lajas','0604','060410',1),('060411','Llama','0604','060411',1),('060412','Miracosta','0604','060412',1),('060413','Paccha','0604','060413',1),('060414','Pion','0604','060414',1),('060415','Querocoto','0604','060415',1),('060416','San Juan de Licupis','0604','060416',1),('060417','Tacabamba','0604','060417',1),('060418','Tocmoche','0604','060418',1),('060419','Chalamarca','0604','060419',1),('060501','Contumaza','0605','060501',1),('060502','Chilete','0605','060502',1),('060503','Cupisnique','0605','060503',1),('060504','Guzmango','0605','060504',1),('060505','San Benito','0605','060505',1),('060506','Santa Cruz de Toled','0605','060506',1),('060507','Tantarica','0605','060507',1),('060508','Yonan','0605','060508',1),('060601','Cutervo','0606','060601',1),('060602','Callayuc','0606','060602',1),('060603','Choros','0606','060603',1),('060604','Cujillo','0606','060604',1),('060605','La Ramada','0606','060605',1),('060606','Pimpingos','0606','060606',1),('060607','Querocotillo','0606','060607',1),('060608','San Andres de Cutervo','0606','060608',1),('060609','San Juan de Cutervo','0606','060609',1),('060610','San Luis de Lucma','0606','060610',1),('060611','Santa Cruz','0606','060611',1),('060612','Santo Domingo de La Capilla','0606','060612',1),('060613','Santo Tomas','0606','060613',1),('060614','Socota','0606','060614',1),('060615','Toribio Casanova','0606','060615',1),('060701','Bambamarca','0607','060701',1),('060702','Chugur','0607','060702',1),('060703','Hualgayoc','0607','060703',1),('060801','Jaen','0608','060801',1),('060802','Bellavista','0608','060802',1),('060803','Chontali','0608','060803',1),('060804','Colasay','0608','060804',1),('060805','Huabal','0608','060805',1),('060806','Las Pirias','0608','060806',1),('060807','Pomahuaca','0608','060807',1),('060808','Pucara','0608','060808',1),('060809','Sallique','0608','060809',1),('060810','San Felipe','0608','060810',1),('060811','San Jose del Alto','0608','060811',1),('060812','Santa Rosa','0608','060812',1),('060901','San Ignacio','0609','060901',1),('060902','Chirinos','0609','060902',1),('060903','Huarango','0609','060903',1),('060904','La Coipa','0609','060904',1),('060905','Namballe','0609','060905',1),('060906','San Jose de Lourdes','0609','060906',1),('060907','Tabaconas','0609','060907',1),('061001','Pedro Galvez','0610','061001',1),('061002','Chancay','0610','061002',1),('061003','Eduardo Villanueva','0610','061003',1),('061004','Gregorio Pita','0610','061004',1),('061005','Ichocan','0610','061005',1),('061006','Jose Manuel Quiroz','0610','061006',1),('061007','Jose Sabogal','0610','061007',1),('061101','San Miguel','0611','061101',1),('061102','Bolivar','0611','061102',1),('061103','Calquis','0611','061103',1),('061104','Catilluc','0611','061104',1),('061105','El Prado','0611','061105',1),('061106','La Florida','0611','061106',1),('061107','Llapa','0611','061107',1),('061108','Nanchoc','0611','061108',1),('061109','Niepos','0611','061109',1),('061110','San Gregorio','0611','061110',1),('061111','San Silvestre de Cochan','0611','061111',1),('061112','Tongod','0611','061112',1),('061113','Union Agua Blanca','0611','061113',1),('061201','San Pablo','0612','061201',1),('061202','San Bernardino','0612','061202',1),('061203','San Luis','0612','061203',1),('061204','Tumbaden','0612','061204',1),('061301','Santa Cruz','0613','061301',1),('061302','Andabamba','0613','061302',1),('061303','Catache','0613','061303',1),('061304','Chancaybaños','0613','061304',1),('061305','La Esperanza','0613','061305',1),('061306','Ninabamba','0613','061306',1),('061307','Pulan','0613','061307',1),('061308','Saucepampa','0613','061308',1),('061309','Sexi','0613','061309',1),('061310','Uticyacu','0613','061310',1),('061311','Yauyucan','0613','061311',1),('070101','Callao','0701','070101',1),('070102','Bellavista','0701','070102',1),('070103','Carmen de La Legua','0701','070103',1),('070104','La Perla','0701','070104',1),('070105','La Punta','0701','070105',1),('070106','Ventanilla','0701','070106',1),('070107','Mi Peru','0701','070107',1),('080101','Cusco','0801','080101',1),('080102','Ccorca','0801','080102',1),('080103','Poroy','0801','080103',1),('080104','San Jeronimo','0801','080104',1),('080105','San Sebastian','0801','080105',1),('080106','Santiago','0801','080106',1),('080107','Saylla','0801','080107',1),('080108','Wanchaq','0801','080108',1),('080201','Acomayo','0802','080201',1),('080202','Acopia','0802','080202',1),('080203','Acos','0802','080203',1),('080204','Mosoc Llacta','0802','080204',1),('080205','Pomacanchi','0802','080205',1),('080206','Rondocan','0802','080206',1),('080207','Sangarara','0802','080207',1),('080301','Anta','0803','080301',1),('080302','Ancahuasi','0803','080302',1),('080303','Cachimayo','0803','080303',1),('080304','Chinchaypujio','0803','080304',1),('080305','Huarocondo','0803','080305',1),('080306','Limatambo','0803','080306',1),('080307','Mollepata','0803','080307',1),('080308','Pucyura','0803','080308',1),('080309','Zurite','0803','080309',1),('080401','Calca','0804','080401',1),('080402','Coya','0804','080402',1),('080403','Lamay','0804','080403',1),('080404','Lares','0804','080404',1),('080405','Pisac','0804','080405',1),('080406','San Salvador','0804','080406',1),('080407','Taray','0804','080407',1),('080408','Yanatile','0804','080408',1),('080501','Yanaoca','0805','080501',1),('080502','Checca','0805','080502',1),('080503','Kunturkanki','0805','080503',1),('080504','Langui','0805','080504',1),('080505','Layo','0805','080505',1),('080506','Pampamarca','0805','080506',1),('080507','Quehue','0805','080507',1),('080508','Tupac Amaru','0805','080508',1),('080601','Sicuani','0806','080601',1),('080602','Checacupe','0806','080602',1),('080603','Combapata','0806','080603',1),('080604','Marangani','0806','080604',1),('080605','Pitumarca','0806','080605',1),('080606','San Pablo','0806','080606',1),('080607','San Pedro','0806','080607',1),('080608','Tinta','0806','080608',1),('080701','Santo Tomas','0807','080701',1),('080702','Capacmarca','0807','080702',1),('080703','Chamaca','0807','080703',1),('080704','Colquemarca','0807','080704',1),('080705','Livitaca','0807','080705',1),('080706','Llusco','0807','080706',1),('080707','Quiñota','0807','080707',1),('080708','Velille','0807','080708',1),('080801','Espinar','0808','080801',1),('080802','Condoroma','0808','080802',1),('080803','Coporaque','0808','080803',1),('080804','Ocoruro','0808','080804',1),('080805','Pallpata','0808','080805',1),('080806','Pichigua','0808','080806',1),('080807','Suyckutambo','0808','080807',1),('080808','Alto Pichigua','0808','080808',1),('080901','Santa Ana','0809','080901',1),('080902','Echarate','0809','080902',1),('080903','Huayopata','0809','080903',1),('080904','Maranura','0809','080904',1),('080905','Ocobamba','0809','080905',1),('080906','Quellouno','0809','080906',1),('080907','Kimbiri','0809','080907',1),('080908','Santa Teresa','0809','080908',1),('080909','Vilcabamba','0809','080909',1),('080910','Pichari','0809','080910',1),('080911','Inkawasi','0809','080911',1),('080912','Villa Virgen','0809','080912',1),('080913','Villa Kintiarina','0809','080913',1),('080914','Megantoni','0809','080914',1),('081001','Paruro','0810','081001',1),('081002','Accha','0810','081002',1),('081003','Ccapi','0810','081003',1),('081004','Colcha','0810','081004',1),('081005','Huanoquite','0810','081005',1),('081006','Omacha','0810','081006',1),('081007','Paccaritambo','0810','081007',1),('081008','Pillpinto','0810','081008',1),('081009','Yaurisque','0810','081009',1),('081101','Paucartambo','0811','081101',1),('081102','Caicay','0811','081102',1),('081103','Challabamba','0811','081103',1),('081104','Colquepata','0811','081104',1),('081105','Huancarani','0811','081105',1),('081106','Kosñipata','0811','081106',1),('081201','Urcos','0812','081201',1),('081202','Andahuaylillas','0812','081202',1),('081203','Camanti','0812','081203',1),('081204','Ccarhuayo','0812','081204',1),('081205','Ccatca','0812','081205',1),('081206','Cusipata','0812','081206',1),('081207','Huaro','0812','081207',1),('081208','Lucre','0812','081208',1),('081209','Marcapata','0812','081209',1),('081210','Ocongate','0812','081210',1),('081211','Oropesa','0812','081211',1),('081212','Quiquijana','0812','081212',1),('081301','Urubamba','0813','081301',1),('081302','Chinchero','0813','081302',1),('081303','Huayllabamba','0813','081303',1),('081304','Machupicchu','0813','081304',1),('081305','Maras','0813','081305',1),('081306','Ollantaytambo','0813','081306',1),('081307','Yucay','0813','081307',1),('090101','Huancavelica','0901','090101',1),('090102','Acobambilla','0901','090102',1),('090103','Acoria','0901','090103',1),('090104','Conayca','0901','090104',1),('090105','Cuenca','0901','090105',1),('090106','Huachocolpa','0901','090106',1),('090107','Huayllahuara','0901','090107',1),('090108','Izcuchaca','0901','090108',1),('090109','Laria','0901','090109',1),('090110','Manta','0901','090110',1),('090111','Mariscal Caceres','0901','090111',1),('090112','Moya','0901','090112',1),('090113','Nuevo Occoro','0901','090113',1),('090114','Palca','0901','090114',1),('090115','Pilchaca','0901','090115',1),('090116','Vilca','0901','090116',1),('090117','Yauli','0901','090117',1),('090118','Ascension','0901','090118',1),('090119','Huando','0901','090119',1),('090201','Acobamba','0902','090201',1),('090202','Andabamba','0902','090202',1),('090203','Anta','0902','090203',1),('090204','Caja','0902','090204',1),('090205','Marcas','0902','090205',1),('090206','Paucara','0902','090206',1),('090207','Pomacocha','0902','090207',1),('090208','Rosario','0902','090208',1),('090301','Lircay','0903','090301',1),('090302','Anchonga','0903','090302',1),('090303','Callanmarca','0903','090303',1),('090304','Ccochaccasa','0903','090304',1),('090305','Chincho','0903','090305',1),('090306','Congalla','0903','090306',1),('090307','Huanca-Huanca','0903','090307',1),('090308','Huayllay Grande','0903','090308',1),('090309','Julcamarca','0903','090309',1),('090310','San Antonio de Antaparco','0903','090310',1),('090311','Santo Tomas de Pata','0903','090311',1),('090312','Secclla','0903','090312',1),('090401','Castrovirreyna','0904','090401',1),('090402','Arma','0904','090402',1),('090403','Aurahua','0904','090403',1),('090404','Capillas','0904','090404',1),('090405','Chupamarca','0904','090405',1),('090406','Cocas','0904','090406',1),('090407','Huachos','0904','090407',1),('090408','Huamatambo','0904','090408',1),('090409','Mollepampa','0904','090409',1),('090410','San Juan','0904','090410',1),('090411','Santa Ana','0904','090411',1),('090412','Tantara','0904','090412',1),('090413','Ticrapo','0904','090413',1),('090501','Churcampa','0905','090501',1),('090502','Anco','0905','090502',1),('090503','Chinchihuasi','0905','090503',1),('090504','El Carmen','0905','090504',1),('090505','La Merced','0905','090505',1),('090506','Locroja','0905','090506',1),('090507','Paucarbamba','0905','090507',1),('090508','San Miguel de Mayocc','0905','090508',1),('090509','San Pedro de Coris','0905','090509',1),('090510','Pachamarca','0905','090510',1),('090511','Cosme','0905','090511',1),('090601','Huaytara','0906','090601',1),('090602','Ayavi','0906','090602',1),('090603','Cordova','0906','090603',1),('090604','Huayacundo Arma','0906','090604',1),('090605','Laramarca','0906','090605',1),('090606','Ocoyo','0906','090606',1),('090607','Pilpichaca','0906','090607',1),('090608','Querco','0906','090608',1),('090609','Quito-Arma','0906','090609',1),('090610','San Antonio de Cusicancha','0906','090610',1),('090611','San Francisco de Sangayaico','0906','090611',1),('090612','San Isidro','0906','090612',1),('090613','Santiago de Chocorvos','0906','090613',1),('090614','Santiago de Quirahuara','0906','090614',1),('090615','Santo Domingo de Capillas','0906','090615',1),('090616','Tambo','0906','090616',1),('090701','Pampas','0907','090701',1),('090702','Acostambo','0907','090702',1),('090703','Acraquia','0907','090703',1),('090704','Ahuaycha','0907','090704',1),('090705','Colcabamba','0907','090705',1),('090706','Daniel Hernandez','0907','090706',1),('090707','Huachocolpa','0907','090707',1),('090709','Huaribamba','0907','090709',1),('090710','Ñahuimpuquio','0907','090710',1),('090711','Pazos','0907','090711',1),('090713','Quishuar','0907','090713',1),('090714','Salcabamba','0907','090714',1),('090715','Salcahuasi','0907','090715',1),('090716','San Marcos de Rocchac','0907','090716',1),('090717','Surcubamba','0907','090717',1),('090718','Tintay Puncu','0907','090718',1),('090719','Quichuas','0907','090719',1),('090720','Andaymarca','0907','090720',1),('090721','Roble','0907','090721',1),('090722','Pichos','0907','090722',1),('090723','Santiago de Túcuma','0907','090723',1),('100101','Huanuco','1001','100101',1),('100102','Amarilis','1001','100102',1),('100103','Chinchao','1001','100103',1),('100104','Churubamba','1001','100104',1),('100105','Margos','1001','100105',1),('100106','Quisqui','1001','100106',1),('100107','San Francisco de Cayran','1001','100107',1),('100108','San Pedro de Chaulan','1001','100108',1),('100109','Santa Maria del Valle','1001','100109',1),('100110','Yarumayo','1001','100110',1),('100111','Pillco Marca','1001','100111',1),('100112','Yacus','1001','100112',1),('100113','San Pablo de Pillao','1001','100113',1),('100201','Ambo','1002','100201',1),('100202','Cayna','1002','100202',1),('100203','Colpas','1002','100203',1),('100204','Conchamarca','1002','100204',1),('100205','Huacar','1002','100205',1),('100206','San Francisco','1002','100206',1),('100207','San Rafael','1002','100207',1),('100208','Tomay Kichwa','1002','100208',1),('100301','La Union','1003','100301',1),('100307','Chuquis','1003','100307',1),('100311','Marias','1003','100311',1),('100313','Pachas','1003','100313',1),('100316','Quivilla','1003','100316',1),('100317','Ripan','1003','100317',1),('100321','Shunqui','1003','100321',1),('100322','Sillapata','1003','100322',1),('100323','Yanas','1003','100323',1),('100401','Huacaybamba','1004','100401',1),('100402','Canchabamba','1004','100402',1),('100403','Cochabamba','1004','100403',1),('100404','Pinra','1004','100404',1),('100501','Llata','1005','100501',1),('100502','Arancay','1005','100502',1),('100503','Chavin de Pariarca','1005','100503',1),('100504','Jacas Grande','1005','100504',1),('100505','Jircan','1005','100505',1),('100506','Miraflores','1005','100506',1),('100507','Monzon','1005','100507',1),('100508','Punchao','1005','100508',1),('100509','Puños','1005','100509',1),('100510','Singa','1005','100510',1),('100511','Tantamayo','1005','100511',1),('100601','Rupa-Rupa','1006','100601',1),('100602','Daniel Alomias Robles','1006','100602',1),('100603','Hermilio Valdizan','1006','100603',1),('100604','Jose Crespo y Castillo','1006','100604',1),('100605','Luyando','1006','100605',1),('100606','Mariano Damaso Beraun','1006','100606',1),('100607','Pucayacu','1006','100607',1),('100608','Castillo Grande','1006','100608',1),('100609','Pueblo Nuevo','1006','100609',1),('100610','Santo Domingo de Anda','1006','100610',1),('100701','Huacrachuco','1007','100701',1),('100702','Cholon','1007','100702',1),('100703','San Buenaventura','1007','100703',1),('100704','La Morada','1007','100704',1),('100705','Santa Rosa de Alto Yanajanca','1007','100705',1),('100801','Panao','1008','100801',1),('100802','Chaglla','1008','100802',1),('100803','Molino','1008','100803',1),('100804','Umari','1008','100804',1),('100901','Puerto Inca','1009','100901',1),('100902','Codo del Pozuzo','1009','100902',1),('100903','Honoria','1009','100903',1),('100904','Tournavista','1009','100904',1),('100905','Yuyapichis','1009','100905',1),('101001','Jesus','1010','101001',1),('101002','Baños','1010','101002',1),('101003','Jivia','1010','101003',1),('101004','Queropalca','1010','101004',1),('101005','Rondos','1010','101005',1),('101006','San Francisco de Asis','1010','101006',1),('101007','San Miguel de Cauri','1010','101007',1),('101101','Chavinillo','1011','101101',1),('101102','Cahuac','1011','101102',1),('101103','Chacabamba','1011','101103',1),('101104','Aparicio Pomares','1011','101104',1),('101105','Jacas Chico','1011','101105',1),('101106','Obas','1011','101106',1),('101107','Pampamarca','1011','101107',1),('101108','Choras','1011','101108',1),('110101','Ica','1101','110101',1),('110102','La Tinguiña','1101','110102',1),('110103','Los Aquijes','1101','110103',1),('110104','Ocucaje','1101','110104',1),('110105','Pachacutec','1101','110105',1),('110106','Parcona','1101','110106',1),('110107','Pueblo Nuevo','1101','110107',1),('110108','Salas','1101','110108',1),('110109','San Jose de los Molinos','1101','110109',1),('110110','San Juan Bautista','1101','110110',1),('110111','Santiago','1101','110111',1),('110112','Subtanjalla','1101','110112',1),('110113','Tate','1101','110113',1),('110114','Yauca del Rosario','1101','110114',1),('110201','Chincha Alta','1102','110201',1),('110202','Alto Laran','1102','110202',1),('110203','Chavin','1102','110203',1),('110204','Chincha Baja','1102','110204',1),('110205','El Carmen','1102','110205',1),('110206','Grocio Prado','1102','110206',1),('110207','Pueblo Nuevo','1102','110207',1),('110208','San Juan de Yanac','1102','110208',1),('110209','San Pedro de Huacarpana','1102','110209',1),('110210','Sunampe','1102','110210',1),('110211','Tambo de Mora','1102','110211',1),('110301','Nazca','1103','110301',1),('110302','Changuillo','1103','110302',1),('110303','El Ingenio','1103','110303',1),('110304','Marcona','1103','110304',1),('110305','Vista Alegre','1103','110305',1),('110401','Palpa','1104','110401',1),('110402','Llipata','1104','110402',1),('110403','Rio Grande','1104','110403',1),('110404','Santa Cruz','1104','110404',1),('110405','Tibillo','1104','110405',1),('110501','Pisco','1105','110501',1),('110502','Huancano','1105','110502',1),('110503','Humay','1105','110503',1),('110504','Independencia','1105','110504',1),('110505','Paracas','1105','110505',1),('110506','San Andres','1105','110506',1),('110507','San Clemente','1105','110507',1),('110508','Tupac Amaru Inca','1105','110508',1),('120101','Huancayo','1201','120101',1),('120104','Carhuacallanga','1201','120104',1),('120105','Chacapampa','1201','120105',1),('120106','Chicche','1201','120106',1),('120107','Chilca','1201','120107',1),('120108','Chongos Alto','1201','120108',1),('120111','Chupuro','1201','120111',1),('120112','Colca','1201','120112',1),('120113','Cullhuas','1201','120113',1),('120114','El Tambo','1201','120114',1),('120116','Huacrapuquio','1201','120116',1),('120117','Hualhuas','1201','120117',1),('120119','Huancan','1201','120119',1),('120120','Huasicancha','1201','120120',1),('120121','Huayucachi','1201','120121',1),('120122','Ingenio','1201','120122',1),('120124','Pariahuanca','1201','120124',1),('120125','Pilcomayo','1201','120125',1),('120126','Pucara','1201','120126',1),('120127','Quichuay','1201','120127',1),('120128','Quilcas','1201','120128',1),('120129','San Agustin','1201','120129',1),('120130','San Jeronimo de Tunan','1201','120130',1),('120132','Saño','1201','120132',1),('120133','Sapallanga','1201','120133',1),('120134','Sicaya','1201','120134',1),('120135','Santo Domingo de Acobamba','1201','120135',1),('120136','Viques','1201','120136',1),('120201','Concepcion','1202','120201',1),('120202','Aco','1202','120202',1),('120203','Andamarca','1202','120203',1),('120204','Chambara','1202','120204',1),('120205','Cochas','1202','120205',1),('120206','Comas','1202','120206',1),('120207','Heroinas Toledo','1202','120207',1),('120208','Manzanares','1202','120208',1),('120209','Mariscal Castilla','1202','120209',1),('120210','Matahuasi','1202','120210',1),('120211','Mito','1202','120211',1),('120212','Nueve de Julio','1202','120212',1),('120213','Orcotuna','1202','120213',1),('120214','San Jose de Quero','1202','120214',1),('120215','Santa Rosa de Ocopa','1202','120215',1),('120301','Chanchamayo','1203','120301',1),('120302','Perene','1203','120302',1),('120303','Pichanaqui','1203','120303',1),('120304','San Luis de Shuaro','1203','120304',1),('120305','San Ramon','1203','120305',1),('120306','Vitoc','1203','120306',1),('120401','Jauja','1204','120401',1),('120402','Acolla','1204','120402',1),('120403','Apata','1204','120403',1),('120404','Ataura','1204','120404',1),('120405','Canchayllo','1204','120405',1),('120406','Curicaca','1204','120406',1),('120407','El Mantaro','1204','120407',1),('120408','Huamali','1204','120408',1),('120409','Huaripampa','1204','120409',1),('120410','Huertas','1204','120410',1),('120411','Janjaillo','1204','120411',1),('120412','Julcan','1204','120412',1),('120413','Leonor Ordoñez','1204','120413',1),('120414','Llocllapampa','1204','120414',1),('120415','Marco','1204','120415',1),('120416','Masma','1204','120416',1),('120417','Masma Chicche','1204','120417',1),('120418','Molinos','1204','120418',1),('120419','Monobamba','1204','120419',1),('120420','Muqui','1204','120420',1),('120421','Muquiyauyo','1204','120421',1),('120422','Paca','1204','120422',1),('120423','Paccha','1204','120423',1),('120424','Pancan','1204','120424',1),('120425','Parco','1204','120425',1),('120426','Pomacancha','1204','120426',1),('120427','Ricran','1204','120427',1),('120428','San Lorenzo','1204','120428',1),('120429','San Pedro de Chunan','1204','120429',1),('120430','Sausa','1204','120430',1),('120431','Sincos','1204','120431',1),('120432','Tunan Marca','1204','120432',1),('120433','Yauli','1204','120433',1),('120434','Yauyos','1204','120434',1),('120501','Junin','1205','120501',1),('120502','Carhuamayo','1205','120502',1),('120503','Ondores','1205','120503',1),('120504','Ulcumayo','1205','120504',1),('120601','Satipo','1206','120601',1),('120602','Coviriali','1206','120602',1),('120603','Llaylla','1206','120603',1),('120604','Mazamari','1206','120604',1),('120605','Pampa Hermosa','1206','120605',1),('120606','Pangoa','1206','120606',1),('120607','Rio Negro','1206','120607',1),('120608','Rio Tambo','1206','120608',1),('120609','Vizcatán del Ene','1206','120609',1),('120701','Tarma','1207','120701',1),('120702','Acobamba','1207','120702',1),('120703','Huaricolca','1207','120703',1),('120704','Huasahuasi','1207','120704',1),('120705','La Union','1207','120705',1),('120706','Palca','1207','120706',1),('120707','Palcamayo','1207','120707',1),('120708','San Pedro de Cajas','1207','120708',1),('120709','Tapo','1207','120709',1),('120801','La Oroya','1208','120801',1),('120802','Chacapalpa','1208','120802',1),('120803','Huay-Huay','1208','120803',1),('120804','Marcapomacocha','1208','120804',1),('120805','Morococha','1208','120805',1),('120806','Paccha','1208','120806',1),('120807','Santa Barbara de Carhuacayan','1208','120807',1),('120808','Santa Rosa de Sacco','1208','120808',1),('120809','Suitucancha','1208','120809',1),('120810','Yauli','1208','120810',1),('120901','Chupaca','1209','120901',1),('120902','Ahuac','1209','120902',1),('120903','Chongos Bajo','1209','120903',1),('120904','Huachac','1209','120904',1),('120905','Huamancaca Chico','1209','120905',1),('120906','San Juan de Yscos','1209','120906',1),('120907','San Juan de Jarpa','1209','120907',1),('120908','Tres de Diciembre','1209','120908',1),('120909','Yanacancha','1209','120909',1),('130101','Trujillo','1301','130101',1),('130102','El Porvenir','1301','130102',1),('130103','Florencia de Mora','1301','130103',1),('130104','Huanchaco','1301','130104',1),('130105','La Esperanza','1301','130105',1),('130106','Laredo','1301','130106',1),('130107','Moche','1301','130107',1),('130108','Poroto','1301','130108',1),('130109','Salaverry','1301','130109',1),('130110','Simbal','1301','130110',1),('130111','Victor Larco Herrera','1301','130111',1),('130201','Ascope','1302','130201',1),('130202','Chicama','1302','130202',1),('130203','Chocope','1302','130203',1),('130204','Magdalena de Cao','1302','130204',1),('130205','Paijan','1302','130205',1),('130206','Razuri','1302','130206',1),('130207','Santiago de Cao','1302','130207',1),('130208','Casa Grande','1302','130208',1),('130301','Bolivar','1303','130301',1),('130302','Bambamarca','1303','130302',1),('130303','Condormarca','1303','130303',1),('130304','Longotea','1303','130304',1),('130305','Uchumarca','1303','130305',1),('130306','Ucuncha','1303','130306',1),('130401','Chepen','1304','130401',1),('130402','Pacanga','1304','130402',1),('130403','Pueblo Nuevo','1304','130403',1),('130501','Julcan','1305','130501',1),('130502','Calamarca','1305','130502',1),('130503','Carabamba','1305','130503',1),('130504','Huaso','1305','130504',1),('130601','Otuzco','1306','130601',1),('130602','Agallpampa','1306','130602',1),('130604','Charat','1306','130604',1),('130605','Huaranchal','1306','130605',1),('130606','La Cuesta','1306','130606',1),('130608','Mache','1306','130608',1),('130610','Paranday','1306','130610',1),('130611','Salpo','1306','130611',1),('130613','Sinsicap','1306','130613',1),('130614','Usquil','1306','130614',1),('130701','San Pedro de Lloc','1307','130701',1),('130702','Guadalupe','1307','130702',1),('130703','Jequetepeque','1307','130703',1),('130704','Pacasmayo','1307','130704',1),('130705','San Jose','1307','130705',1),('130801','Tayabamba','1308','130801',1),('130802','Buldibuyo','1308','130802',1),('130803','Chillia','1308','130803',1),('130804','Huancaspata','1308','130804',1),('130805','Huaylillas','1308','130805',1),('130806','Huayo','1308','130806',1),('130807','Ongon','1308','130807',1),('130808','Parcoy','1308','130808',1),('130809','Pataz','1308','130809',1),('130810','Pias','1308','130810',1),('130811','Santiago de Challas','1308','130811',1),('130812','Taurija','1308','130812',1),('130813','Urpay','1308','130813',1),('130901','Huamachuco','1309','130901',1),('130902','Chugay','1309','130902',1),('130903','Cochorco','1309','130903',1),('130904','Curgos','1309','130904',1),('130905','Marcabal','1309','130905',1),('130906','Sanagoran','1309','130906',1),('130907','Sarin','1309','130907',1),('130908','Sartimbamba','1309','130908',1),('131001','Santiago de Chuco','1310','131001',1),('131002','Angasmarca','1310','131002',1),('131003','Cachicadan','1310','131003',1),('131004','Mollebamba','1310','131004',1),('131005','Mollepata','1310','131005',1),('131006','Quiruvilca','1310','131006',1),('131007','Santa Cruz de Chuca','1310','131007',1),('131008','Sitabamba','1310','131008',1),('131101','Cascas','1311','131101',1),('131102','Lucma','1311','131102',1),('131103','Compin','1311','131103',1),('131104','Sayapullo','1311','131104',1),('131201','Viru','1312','131201',1),('131202','Chao','1312','131202',1),('131203','Guadalupito','1312','131203',1),('140101','Chiclayo','1401','140101',1),('140102','Chongoyape','1401','140102',1),('140103','Eten','1401','140103',1),('140104','Eten Puerto','1401','140104',1),('140105','Jose Leonardo Ortiz','1401','140105',1),('140106','La Victoria','1401','140106',1),('140107','Lagunas','1401','140107',1),('140108','Monsefu','1401','140108',1),('140109','Nueva Arica','1401','140109',1),('140110','Oyotun','1401','140110',1),('140111','Picsi','1401','140111',1),('140112','Pimentel','1401','140112',1),('140113','Reque','1401','140113',1),('140114','Santa Rosa','1401','140114',1),('140115','Saña','1401','140115',1),('140116','Cayalti','1401','140116',1),('140117','Patapo','1401','140117',1),('140118','Pomalca','1401','140118',1),('140119','Pucala','1401','140119',1),('140120','Tuman','1401','140120',1),('140201','Ferreñafe','1402','140201',1),('140202','Cañaris','1402','140202',1),('140203','Incahuasi','1402','140203',1),('140204','Manuel Antonio Mesones Muro','1402','140204',1),('140205','Pitipo','1402','140205',1),('140206','Pueblo Nuevo','1402','140206',1),('140301','Lambayeque','1403','140301',1),('140302','Chochope','1403','140302',1),('140303','Illimo','1403','140303',1),('140304','Jayanca','1403','140304',1),('140305','Mochumi','1403','140305',1),('140306','Morrope','1403','140306',1),('140307','Motupe','1403','140307',1),('140308','Olmos','1403','140308',1),('140309','Pacora','1403','140309',1),('140310','Salas','1403','140310',1),('140311','San Jose','1403','140311',1),('140312','Tucume','1403','140312',1),('150101','Lima','1501','150101',1),('150102','Ancon','1501','150102',1),('150103','Ate','1501','150103',1),('150104','Barranco','1501','150104',1),('150105','Breña','1501','150105',1),('150106','Carabayllo','1501','150106',1),('150107','Chaclacayo','1501','150107',1),('150108','Chorrillos','1501','150108',1),('150109','Cieneguilla','1501','150109',1),('150110','Comas','1501','150110',1),('150111','El Agustino','1501','150111',1),('150112','Independencia','1501','150112',1),('150113','Jesus Maria','1501','150113',1),('150114','La Molina','1501','150114',1),('150115','La Victoria','1501','150115',1),('150116','Lince','1501','150116',1),('150117','Los Olivos','1501','150117',1),('150118','Lurigancho','1501','150118',1),('150119','Lurin','1501','150119',1),('150120','Magdalena del Mar','1501','150120',1),('150121','Pueblo Libre','1501','150121',1),('150122','Miraflores','1501','150122',1),('150123','Pachacamac','1501','150123',1),('150124','Pucusana','1501','150124',1),('150125','Puente Piedra','1501','150125',1),('150126','Punta Hermosa','1501','150126',1),('150127','Punta Negra','1501','150127',1),('150128','Rimac','1501','150128',1),('150129','San Bartolo','1501','150129',1),('150130','San Borja','1501','150130',1),('150131','San Isidro','1501','150131',1),('150132','San Juan de Lurigancho','1501','150132',1),('150133','San Juan de Miraflores','1501','150133',1),('150134','San Luis','1501','150134',1),('150135','San Martin de Porres','1501','150135',1),('150136','San Miguel','1501','150136',1),('150137','Santa Anita','1501','150137',1),('150138','Santa Maria del Mar','1501','150138',1),('150139','Santa Rosa','1501','150139',1),('150140','Santiago de Surco','1501','150140',1),('150141','Surquillo','1501','150141',1),('150142','Villa El Salvador','1501','150142',1),('150143','Villa Maria del Triunfo','1501','150143',1),('150201','Barranca','1502','150201',1),('150202','Paramonga','1502','150202',1),('150203','Pativilca','1502','150203',1),('150204','Supe','1502','150204',1),('150205','Supe Puerto','1502','150205',1),('150301','Cajatambo','1503','150301',1),('150302','Copa','1503','150302',1),('150303','Gorgor','1503','150303',1),('150304','Huancapon','1503','150304',1),('150305','Manas','1503','150305',1),('150401','Canta','1504','150401',1),('150402','Arahuay','1504','150402',1),('150403','Huamantanga','1504','150403',1),('150404','Huaros','1504','150404',1),('150405','Lachaqui','1504','150405',1),('150406','San Buenaventura','1504','150406',1),('150407','Santa Rosa de Quives','1504','150407',1),('150501','San Vicente de Cañete','1505','150501',1),('150502','Asia','1505','150502',1),('150503','Calango','1505','150503',1),('150504','Cerro Azul','1505','150504',1),('150505','Chilca','1505','150505',1),('150506','Coayllo','1505','150506',1),('150507','Imperial','1505','150507',1),('150508','Lunahuana','1505','150508',1),('150509','Mala','1505','150509',1),('150510','Nuevo Imperial','1505','150510',1),('150511','Pacaran','1505','150511',1),('150512','Quilmana','1505','150512',1),('150513','San Antonio','1505','150513',1),('150514','San Luis','1505','150514',1),('150515','Santa Cruz de Flores','1505','150515',1),('150516','Zuñiga','1505','150516',1),('150601','Huaral','1506','150601',1),('150602','Atavillos Alto','1506','150602',1),('150603','Atavillos Bajo','1506','150603',1),('150604','Aucallama','1506','150604',1),('150605','Chancay','1506','150605',1),('150606','Ihuari','1506','150606',1),('150607','Lampian','1506','150607',1),('150608','Pacaraos','1506','150608',1),('150609','San Miguel de Acos','1506','150609',1),('150610','Santa Cruz de Andamarca','1506','150610',1),('150611','Sumbilca','1506','150611',1),('150612','Veintisiete de Noviembre','1506','150612',1),('150701','Matucana','1507','150701',1),('150702','Antioquia','1507','150702',1),('150703','Callahuanca','1507','150703',1),('150704','Carampoma','1507','150704',1),('150705','Chicla','1507','150705',1),('150706','Cuenca','1507','150706',1),('150707','Huachupampa','1507','150707',1),('150708','Huanza','1507','150708',1),('150709','Huarochiri','1507','150709',1),('150710','Lahuaytambo','1507','150710',1),('150711','Langa','1507','150711',1),('150712','Laraos','1507','150712',1),('150713','Mariatana','1507','150713',1),('150714','Ricardo Palma','1507','150714',1),('150715','San Andres de Tupicocha','1507','150715',1),('150716','San Antonio','1507','150716',1),('150717','San Bartolome','1507','150717',1),('150718','San Damian','1507','150718',1),('150719','San Juan de Iris','1507','150719',1),('150720','San Juan de Tantaranche','1507','150720',1),('150721','San Lorenzo de Quinti','1507','150721',1),('150722','San Mateo','1507','150722',1),('150723','San Mateo de Otao','1507','150723',1),('150724','San Pedro de Casta','1507','150724',1),('150725','San Pedro de Huancayre','1507','150725',1),('150726','Sangallaya','1507','150726',1),('150727','Santa Cruz de Cocachacra','1507','150727',1),('150728','Santa Eulalia','1507','150728',1),('150729','Santiago de Anchucaya','1507','150729',1),('150730','Santiago de Tuna','1507','150730',1),('150731','Santo Domingo de los Olleros','1507','150731',1),('150732','Surco','1507','150732',1),('150801','Huacho','1508','150801',1),('150802','Ambar','1508','150802',1),('150803','Caleta de Carquin','1508','150803',1),('150804','Checras','1508','150804',1),('150805','Hualmay','1508','150805',1),('150806','Huaura','1508','150806',1),('150807','Leoncio Prado','1508','150807',1),('150808','Paccho','1508','150808',1),('150809','Santa Leonor','1508','150809',1),('150810','Santa Maria','1508','150810',1),('150811','Sayan','1508','150811',1),('150812','Vegueta','1508','150812',1),('150901','Oyon','1509','150901',1),('150902','Andajes','1509','150902',1),('150903','Caujul','1509','150903',1),('150904','Cochamarca','1509','150904',1),('150905','Navan','1509','150905',1),('150906','Pachangara','1509','150906',1),('151001','Yauyos','1510','151001',1),('151002','Alis','1510','151002',1),('151003','Ayauca','1510','151003',1),('151004','Ayaviri','1510','151004',1),('151005','Azangaro','1510','151005',1),('151006','Cacra','1510','151006',1),('151007','Carania','1510','151007',1),('151008','Catahuasi','1510','151008',1),('151009','Chocos','1510','151009',1),('151010','Cochas','1510','151010',1),('151011','Colonia','1510','151011',1),('151012','Hongos','1510','151012',1),('151013','Huampara','1510','151013',1),('151014','Huancaya','1510','151014',1),('151015','Huangascar','1510','151015',1),('151016','Huantan','1510','151016',1),('151017','Huañec','1510','151017',1),('151018','Laraos','1510','151018',1),('151019','Lincha','1510','151019',1),('151020','Madean','1510','151020',1),('151021','Miraflores','1510','151021',1),('151022','Omas','1510','151022',1),('151023','Putinza','1510','151023',1),('151024','Quinches','1510','151024',1),('151025','Quinocay','1510','151025',1),('151026','San Joaquin','1510','151026',1),('151027','San Pedro de Pilas','1510','151027',1),('151028','Tanta','1510','151028',1),('151029','Tauripampa','1510','151029',1),('151030','Tomas','1510','151030',1),('151031','Tupe','1510','151031',1),('151032','Viñac','1510','151032',1),('151033','Vitis','1510','151033',1),('160101','Iquitos','1601','160101',1),('160102','Alto Nanay','1601','160102',1),('160103','Fernando Lores','1601','160103',1),('160104','Indiana','1601','160104',1),('160105','Las Amazonas','1601','160105',1),('160106','Mazan','1601','160106',1),('160107','Napo','1601','160107',1),('160108','Punchana','1601','160108',1),('160110','Torres Causana','1601','160110',1),('160112','Belen','1601','160112',1),('160113','San Juan Bautista','1601','160113',1),('160201','Yurimaguas','1602','160201',1),('160202','Balsapuerto','1602','160202',1),('160205','Jeberos','1602','160205',1),('160206','Lagunas','1602','160206',1),('160210','Santa Cruz','1602','160210',1),('160211','Teniente Cesar Lopez Rojas','1602','160211',1),('160301','Nauta','1603','160301',1),('160302','Parinari','1603','160302',1),('160303','Tigre','1603','160303',1),('160304','Trompeteros','1603','160304',1),('160305','Urarinas','1603','160305',1),('160401','Ramon Castilla','1604','160401',1),('160402','Pebas','1604','160402',1),('160403','Yavari','1604','160403',1),('160404','San Pablo','1604','160404',1),('160501','Requena','1605','160501',1),('160502','Alto Tapiche','1605','160502',1),('160503','Capelo','1605','160503',1),('160504','Emilio San Martin','1605','160504',1),('160505','Maquia','1605','160505',1),('160506','Puinahua','1605','160506',1),('160507','Saquena','1605','160507',1),('160508','Soplin','1605','160508',1),('160509','Tapiche','1605','160509',1),('160510','Jenaro Herrera','1605','160510',1),('160511','Yaquerana','1605','160511',1),('160601','Contamana','1606','160601',1),('160602','Inahuaya','1606','160602',1),('160603','Padre Marquez','1606','160603',1),('160604','Pampa Hermosa','1606','160604',1),('160605','Sarayacu','1606','160605',1),('160606','Vargas Guerra','1606','160606',1),('160701','Barranca','1607','160701',1),('160702','Cahuapanas','1607','160702',1),('160703','Manseriche','1607','160703',1),('160704','Morona','1607','160704',1),('160705','Pastaza','1607','160705',1),('160706','Andoas','1607','160706',1),('160801','Putumayo','1608','160801',1),('160802','Rosa Panduro','1608','160802',1),('160803','Teniente Manuel Clavero','1608','160803',1),('160804','Yaguas','1608','160804',1),('170101','Tambopata','1701','170101',1),('170102','Inambari','1701','170102',1),('170103','Las Piedras','1701','170103',1),('170104','Laberinto','1701','170104',1),('170201','Manu','1702','170201',1),('170202','Fitzcarrald','1702','170202',1),('170203','Madre de Dios','1702','170203',1),('170204','Huepetuhe','1702','170204',1),('170301','Iñapari','1703','170301',1),('170302','Iberia','1703','170302',1),('170303','Tahuamanu','1703','170303',1),('180101','Moquegua','1801','180101',1),('180102','Carumas','1801','180102',1),('180103','Cuchumbaya','1801','180103',1),('180104','Samegua','1801','180104',1),('180105','San Cristobal','1801','180105',1),('180106','Torata','1801','180106',1),('180201','Omate','1802','180201',1),('180202','Chojata','1802','180202',1),('180203','Coalaque','1802','180203',1),('180204','Ichuña','1802','180204',1),('180205','La Capilla','1802','180205',1),('180206','Lloque','1802','180206',1),('180207','Matalaque','1802','180207',1),('180208','Puquina','1802','180208',1),('180209','Quinistaquillas','1802','180209',1),('180210','Ubinas','1802','180210',1),('180211','Yunga','1802','180211',1),('180301','Ilo','1803','180301',1),('180302','El Algarrobal','1803','180302',1),('180303','Pacocha','1803','180303',1),('190101','Chaupimarca','1901','190101',1),('190102','Huachon','1901','190102',1),('190103','Huariaca','1901','190103',1),('190104','Huayllay','1901','190104',1),('190105','Ninacaca','1901','190105',1),('190106','Pallanchacra','1901','190106',1),('190107','Paucartambo','1901','190107',1),('190108','San Francisco de Asis de Yarusyacan','1901','190108',1),('190109','Simon Bolivar','1901','190109',1),('190110','Ticlacayan','1901','190110',1),('190111','Tinyahuarco','1901','190111',1),('190112','Vicco','1901','190112',1),('190113','Yanacancha','1901','190113',1),('190201','Yanahuanca','1902','190201',1),('190202','Chacayan','1902','190202',1),('190203','Goyllarisquizga','1902','190203',1),('190204','Paucar','1902','190204',1),('190205','San Pedro de Pillao','1902','190205',1),('190206','Santa Ana de Tusi','1902','190206',1),('190207','Tapuc','1902','190207',1),('190208','Vilcabamba','1902','190208',1),('190301','Oxapampa','1903','190301',1),('190302','Chontabamba','1903','190302',1),('190303','Huancabamba','1903','190303',1),('190304','Palcazu','1903','190304',1),('190305','Pozuzo','1903','190305',1),('190306','Puerto Bermudez','1903','190306',1),('190307','Villa Rica','1903','190307',1),('190308','Constitución','1903','190308',1),('200101','Piura','2001','200101',1),('200104','Castilla','2001','200104',1),('200105','Catacaos','2001','200105',1),('200107','Cura Mori','2001','200107',1),('200108','El Tallan','2001','200108',1),('200109','La Arena','2001','200109',1),('200110','La Union','2001','200110',1),('200111','Las Lomas','2001','200111',1),('200114','Tambo Grande','2001','200114',1),('200115','26 de octubre','2001','200115',1),('200201','Ayabaca','2002','200201',1),('200202','Frias','2002','200202',1),('200203','Jilili','2002','200203',1),('200204','Lagunas','2002','200204',1),('200205','Montero','2002','200205',1),('200206','Pacaipampa','2002','200206',1),('200207','Paimas','2002','200207',1),('200208','Sapillica','2002','200208',1),('200209','Sicchez','2002','200209',1),('200210','Suyo','2002','200210',1),('200301','Huancabamba','2003','200301',1),('200302','Canchaque','2003','200302',1),('200303','El Carmen de La Frontera','2003','200303',1),('200304','Huarmaca','2003','200304',1),('200305','Lalaquiz','2003','200305',1),('200306','San Miguel de El Faique','2003','200306',1),('200307','Sondor','2003','200307',1),('200308','Sondorillo','2003','200308',1),('200401','Chulucanas','2004','200401',1),('200402','Buenos Aires','2004','200402',1),('200403','Chalaco','2004','200403',1),('200404','La Matanza','2004','200404',1),('200405','Morropon','2004','200405',1),('200406','Salitral','2004','200406',1),('200407','San Juan de Bigote','2004','200407',1),('200408','Santa Catalina de Mossa','2004','200408',1),('200409','Santo Domingo','2004','200409',1),('200410','Yamango','2004','200410',1),('200501','Paita','2005','200501',1),('200502','Amotape','2005','200502',1),('200503','Arenal','2005','200503',1),('200504','Colan','2005','200504',1),('200505','La Huaca','2005','200505',1),('200506','Tamarindo','2005','200506',1),('200507','Vichayal','2005','200507',1),('200601','Sullana','2006','200601',1),('200602','Bellavista','2006','200602',1),('200603','Ignacio Escudero','2006','200603',1),('200604','Lancones','2006','200604',1),('200605','Marcavelica','2006','200605',1),('200606','Miguel Checa','2006','200606',1),('200607','Querecotillo','2006','200607',1),('200608','Salitral','2006','200608',1),('200701','Pariñas','2007','200701',1),('200702','El Alto','2007','200702',1),('200703','La Brea','2007','200703',1),('200704','Lobitos','2007','200704',1),('200705','Los Organos','2007','200705',1),('200706','Mancora','2007','200706',1),('200801','Sechura','2008','200801',1),('200802','Bellavista de La Union','2008','200802',1),('200803','Bernal','2008','200803',1),('200804','Cristo Nos Valga','2008','200804',1),('200805','Vice','2008','200805',1),('200806','Rinconada Llicuar','2008','200806',1),('210101','Puno','2101','210101',1),('210102','Acora','2101','210102',1),('210103','Amantani','2101','210103',1),('210104','Atuncolla','2101','210104',1),('210105','Capachica','2101','210105',1),('210106','Chucuito','2101','210106',1),('210107','Coata','2101','210107',1),('210108','Huata','2101','210108',1),('210109','Mañazo','2101','210109',1),('210110','Paucarcolla','2101','210110',1),('210111','Pichacani','2101','210111',1),('210112','Plateria','2101','210112',1),('210113','San Antonio','2101','210113',1),('210114','Tiquillaca','2101','210114',1),('210115','Vilque','2101','210115',1),('210201','Azangaro','2102','210201',1),('210202','Achaya','2102','210202',1),('210203','Arapa','2102','210203',1),('210204','Asillo','2102','210204',1),('210205','Caminaca','2102','210205',1),('210206','Chupa','2102','210206',1),('210207','Jose Domingo Choquehuanca','2102','210207',1),('210208','Muñani','2102','210208',1),('210209','Potoni','2102','210209',1),('210210','Saman','2102','210210',1),('210211','San Anton','2102','210211',1),('210212','San Jose','2102','210212',1),('210213','San Juan de Salinas','2102','210213',1),('210214','Santiago de Pupuja','2102','210214',1),('210215','Tirapata','2102','210215',1),('210301','Macusani','2103','210301',1),('210302','Ajoyani','2103','210302',1),('210303','Ayapata','2103','210303',1),('210304','Coasa','2103','210304',1),('210305','Corani','2103','210305',1),('210306','Crucero','2103','210306',1),('210307','Ituata','2103','210307',1),('210308','Ollachea','2103','210308',1),('210309','San Gaban','2103','210309',1),('210310','Usicayos','2103','210310',1),('210401','Juli','2104','210401',1),('210402','Desaguadero','2104','210402',1),('210403','Huacullani','2104','210403',1),('210404','Kelluyo','2104','210404',1),('210405','Pisacoma','2104','210405',1),('210406','Pomata','2104','210406',1),('210407','Zepita','2104','210407',1),('210501','Ilave','2105','210501',1),('210502','Capazo','2105','210502',1),('210503','Pilcuyo','2105','210503',1),('210504','Santa Rosa','2105','210504',1),('210505','Conduriri','2105','210505',1),('210601','Huancane','2106','210601',1),('210602','Cojata','2106','210602',1),('210603','Huatasani','2106','210603',1),('210604','Inchupalla','2106','210604',1),('210605','Pusi','2106','210605',1),('210606','Rosaspata','2106','210606',1),('210607','Taraco','2106','210607',1),('210608','Vilque Chico','2106','210608',1),('210701','Lampa','2107','210701',1),('210702','Cabanilla','2107','210702',1),('210703','Calapuja','2107','210703',1),('210704','Nicasio','2107','210704',1),('210705','Ocuviri','2107','210705',1),('210706','Palca','2107','210706',1),('210707','Paratia','2107','210707',1),('210708','Pucara','2107','210708',1),('210709','Santa Lucia','2107','210709',1),('210710','Vilavila','2107','210710',1),('210801','Ayaviri','2108','210801',1),('210802','Antauta','2108','210802',1),('210803','Cupi','2108','210803',1),('210804','Llalli','2108','210804',1),('210805','Macari','2108','210805',1),('210806','Nuñoa','2108','210806',1),('210807','Orurillo','2108','210807',1),('210808','Santa Rosa','2108','210808',1),('210809','Umachiri','2108','210809',1),('210901','Moho','2109','210901',1),('210902','Conima','2109','210902',1),('210903','Huayrapata','2109','210903',1),('210904','Tilali','2109','210904',1),('211001','Putina','2110','211001',1),('211002','Ananea','2110','211002',1),('211003','Pedro Vilca Apaza','2110','211003',1),('211004','Quilcapuncu','2110','211004',1),('211005','Sina','2110','211005',1),('211101','Juliaca','2111','211101',1),('211102','Cabana','2111','211102',1),('211103','Cabanillas','2111','211103',1),('211104','Caracoto','2111','211104',1),('211105','San Miguel','2111','211105',1),('211201','Sandia','2112','211201',1),('211202','Cuyocuyo','2112','211202',1),('211203','Limbani','2112','211203',1),('211204','Patambuco','2112','211204',1),('211205','Phara','2112','211205',1),('211206','Quiaca','2112','211206',1),('211207','San Juan del Oro','2112','211207',1),('211208','Yanahuaya','2112','211208',1),('211209','Alto Inambari','2112','211209',1),('211210','San Pedro de Putina Punco','2112','211210',1),('211301','Yunguyo','2113','211301',1),('211302','Anapia','2113','211302',1),('211303','Copani','2113','211303',1),('211304','Cuturapi','2113','211304',1),('211305','Ollaraya','2113','211305',1),('211306','Tinicachi','2113','211306',1),('211307','Unicachi','2113','211307',1),('220101','Moyobamba','2201','220101',1),('220102','Calzada','2201','220102',1),('220103','Habana','2201','220103',1),('220104','Jepelacio','2201','220104',1),('220105','Soritor','2201','220105',1),('220106','Yantalo','2201','220106',1),('220201','Bellavista','2202','220201',1),('220202','Alto Biavo','2202','220202',1),('220203','Bajo Biavo','2202','220203',1),('220204','Huallaga','2202','220204',1),('220205','San Pablo','2202','220205',1),('220206','San Rafael','2202','220206',1),('220301','San Jose de Sisa','2203','220301',1),('220302','Agua Blanca','2203','220302',1),('220303','San Martin','2203','220303',1),('220304','Santa Rosa','2203','220304',1),('220305','Shatoja','2203','220305',1),('220401','Saposoa','2204','220401',1),('220402','Alto Saposoa','2204','220402',1),('220403','El Eslabon','2204','220403',1),('220404','Piscoyacu','2204','220404',1),('220405','Sacanche','2204','220405',1),('220406','Tingo de Saposoa','2204','220406',1),('220501','Lamas','2205','220501',1),('220502','Alonso de Alvarado','2205','220502',1),('220503','Barranquita','2205','220503',1),('220504','Caynarachi','2205','220504',1),('220505','Cuñumbuqui','2205','220505',1),('220506','Pinto Recodo','2205','220506',1),('220507','Rumisapa','2205','220507',1),('220508','San Roque de Cumbaza','2205','220508',1),('220509','Shanao','2205','220509',1),('220510','Tabalosos','2205','220510',1),('220511','Zapatero','2205','220511',1),('220601','Juanjui','2206','220601',1),('220602','Campanilla','2206','220602',1),('220603','Huicungo','2206','220603',1),('220604','Pachiza','2206','220604',1),('220605','Pajarillo','2206','220605',1),('220701','Picota','2207','220701',1),('220702','Buenos Aires','2207','220702',1),('220703','Caspisapa','2207','220703',1),('220704','Pilluana','2207','220704',1),('220705','Pucacaca','2207','220705',1),('220706','San Cristobal','2207','220706',1),('220707','San Hilarion','2207','220707',1),('220708','Shamboyacu','2207','220708',1),('220709','Tingo de Ponasa','2207','220709',1),('220710','Tres Unidos','2207','220710',1),('220801','Rioja','2208','220801',1),('220802','Awajun','2208','220802',1),('220803','Elias Soplin Vargas','2208','220803',1),('220804','Nueva Cajamarca','2208','220804',1),('220805','Pardo Miguel','2208','220805',1),('220806','Posic','2208','220806',1),('220807','San Fernando','2208','220807',1),('220808','Yorongos','2208','220808',1),('220809','Yuracyacu','2208','220809',1),('220901','Tarapoto','2209','220901',1),('220902','Alberto Leveau','2209','220902',1),('220903','Cacatachi','2209','220903',1),('220904','Chazuta','2209','220904',1),('220905','Chipurana','2209','220905',1),('220906','El Porvenir','2209','220906',1),('220907','Huimbayoc','2209','220907',1),('220908','Juan Guerra','2209','220908',1),('220909','La Banda de Shilcayo','2209','220909',1),('220910','Morales','2209','220910',1),('220911','Papaplaya','2209','220911',1),('220912','San Antonio','2209','220912',1),('220913','Sauce','2209','220913',1),('220914','Shapaja','2209','220914',1),('221001','Tocache','2210','221001',1),('221002','Nuevo Progreso','2210','221002',1),('221003','Polvora','2210','221003',1),('221004','Shunte','2210','221004',1),('221005','Uchiza','2210','221005',1),('230101','Tacna','2301','230101',1),('230102','Alto de La Alianza','2301','230102',1),('230103','Calana','2301','230103',1),('230104','Ciudad Nueva','2301','230104',1),('230105','Inclan','2301','230105',1),('230106','Pachia','2301','230106',1),('230107','Palca','2301','230107',1),('230108','Pocollay','2301','230108',1),('230109','Sama','2301','230109',1),('230110','Coronel Gregorio Albarracin Lanchipa','2301','230110',1),('230111','La Yarada-Los Palos','2301','230111',1),('230201','Candarave','2302','230201',1),('230202','Cairani','2302','230202',1),('230203','Camilaca','2302','230203',1),('230204','Curibaya','2302','230204',1),('230205','Huanuara','2302','230205',1),('230206','Quilahuani','2302','230206',1),('230301','Locumba','2303','230301',1),('230302','Ilabaya','2303','230302',1),('230303','Ite','2303','230303',1),('230401','Tarata','2304','230401',1),('230402','Heroes Albarracin','2304','230402',1),('230403','Estique','2304','230403',1),('230404','Estique-Pampa','2304','230404',1),('230405','Sitajara','2304','230405',1),('230406','Susapaya','2304','230406',1),('230407','Tarucachi','2304','230407',1),('230408','Ticaco','2304','230408',1),('240101','Tumbes','2401','240101',1),('240102','Corrales','2401','240102',1),('240103','La Cruz','2401','240103',1),('240104','Pampas de Hospital','2401','240104',1),('240105','San Jacinto','2401','240105',1),('240106','San Juan de La Virgen','2401','240106',1),('240201','Zorritos','2402','240201',1),('240202','Casitas','2402','240202',1),('240203','Canoas de Punta Sal','2402','240203',1),('240301','Zarumilla','2403','240301',1),('240302','Aguas Verdes','2403','240302',1),('240303','Matapalo','2403','240303',1),('240304','Papayal','2403','240304',1),('250101','Calleria','2501','250101',1),('250102','Campoverde','2501','250102',1),('250103','Iparia','2501','250103',1),('250104','Masisea','2501','250104',1),('250105','Yarinacocha','2501','250105',1),('250106','Nueva Requena','2501','250106',1),('250107','Manantay','2501','250107',1),('250201','Raymondi','2502','250201',1),('250202','Sepahua','2502','250202',1),('250203','Tahuania','2502','250203',1),('250204','Yurua','2502','250204',1),('250301','Padre Abad','2503','250301',1),('250302','Irazola','2503','250302',1),('250303','Curimana','2503','250303',1),('250304','Neshuya','2503','250304',1),('250305','Alexander von Humboldt','2503','250305',1),('250401','Purus','2504','250401',1);
/*!40000 ALTER TABLE `distritos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(8,'software','categoria'),(9,'software','clientes'),(10,'software','codigocorreo'),(11,'software','compradetalle'),(12,'software','compras'),(13,'software','departamentos'),(14,'software','detallecategoriaxunidades'),(15,'software','detalletipousuarioxmodulos'),(16,'software','distritos'),(34,'software','empleado'),(33,'software','empresa'),(17,'software','lotes'),(18,'software','modopago'),(19,'software','modulos'),(20,'software','numserie'),(21,'software','producto'),(22,'software','proveedores'),(23,'software','provincias'),(7,'software','subirdocumentoimagen'),(24,'software','tipocliente'),(25,'software','tipodocumento'),(26,'software','tipoentidad'),(27,'software','tipoigv'),(28,'software','tipousuario'),(29,'software','unidades'),(30,'software','usuario'),(31,'software','venta'),(32,'software','ventadetalle');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-06-05 02:51:05.886786'),(2,'auth','0001_initial','2024-06-05 02:51:06.128189'),(3,'admin','0001_initial','2024-06-05 02:51:06.196980'),(4,'admin','0002_logentry_remove_auto_add','2024-06-05 02:51:06.204016'),(5,'admin','0003_logentry_add_action_flag_choices','2024-06-05 02:51:06.211528'),(6,'contenttypes','0002_remove_content_type_name','2024-06-05 02:51:06.268189'),(7,'auth','0002_alter_permission_name_max_length','2024-06-05 02:51:06.300231'),(8,'auth','0003_alter_user_email_max_length','2024-06-05 02:51:06.325259'),(9,'auth','0004_alter_user_username_opts','2024-06-05 02:51:06.332768'),(10,'auth','0005_alter_user_last_login_null','2024-06-05 02:51:06.370661'),(11,'auth','0006_require_contenttypes_0002','2024-06-05 02:51:06.371657'),(12,'auth','0007_alter_validators_add_error_messages','2024-06-05 02:51:06.378595'),(13,'auth','0008_alter_user_username_max_length','2024-06-05 02:51:06.417967'),(14,'auth','0009_alter_user_last_name_max_length','2024-06-05 02:51:06.455141'),(15,'auth','0010_alter_group_name_max_length','2024-06-05 02:51:06.473078'),(16,'auth','0011_update_proxy_permissions','2024-06-05 02:51:06.481843'),(17,'auth','0012_alter_user_first_name_max_length','2024-06-05 02:51:06.519694'),(18,'sessions','0001_initial','2024-06-05 02:51:06.540307'),(19,'software','0001_initial','2024-06-05 02:51:06.543044'),(20,'software','0002_categoria_clientes_codigocorreo_compradetalle_and_more','2024-07-11 03:14:13.026744'),(21,'software','0003_venta_ruta_xml','2026-04-17 21:14:39.219190');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('07kd63rg3c0dx5zdel5c1k3ne49bmdsn','eyJpZHRpcG91c3VhcmlvIjoxfQ:1sQY8q:hd3WiSYvzx3JWT_VwKEWZ4BRnNniiBlGTgePZFhv9jA','2024-07-21 20:05:48.895633'),('3b7lvpri26chlhg2eyh9o5y5d5n9m6fb','eyJpZHRpcG91c3VhcmlvIjoxLCJub21icmVjb21wbGV0byI6IkNyaXN0aWFuIE1lc3RhbnphIE9ydGl6IiwiaWR1c3VhcmlvIjoyfQ:1wAb6A:u98mTF4sU45JKzmxuPI_A6GZ4_GACijHXmFkRWBsrkw','2026-04-22 22:10:10.736337'),('4muylhhtdx1ahxm1kiqgur6uz37yfzuj','eyJpZHRpcG91c3VhcmlvIjoxLCJub21icmVjb21wbGV0byI6IkNyaXN0aWFuIE1lc3RhbnphIE9ydGl6IiwiaWR1c3VhcmlvIjoyfQ:1wEyA4:BE6AEzmY2GRdFeDEIKiiCJpjCbfQmPEF2Rk_Qdgs950','2026-05-04 23:36:16.824212'),('8dbt99r1b41p6n3a9chcr86m2x565yqm','.eJw9y80KgkAQAOBXkTl7aA0SOirhJRGEljrJrG41_uza7lhi9e556vrB9wZqmEY7-QkdWdiLEIwdlNO1HcZe80qQOvJMaIJce0azYFA4pgXCNf9jFAKOVLHttFmP2Hz8ZJArpRmr7HLblYlsh1NJ56yY5ZPUIafexMmrOT7quksTSfNdXCPUsdrC9weQsTZB:1wABYG:9C9OwbO53rby8P-5-Rrq6IpPn-O_-ABbj_eHLrOqwUM','2026-04-21 18:53:28.800643'),('chdw5n7j97geinghfmiqrkgtkugoxr6y','.eJw9jDkOgDAMwL6CMneBkZUZ8QQUSoZI9FCOpYi_UxZGW7Jv4NO4FldH4QLzOAbIJR1CsaR6kXUHi7AaYx5WUsPccNjEuEHo9V9OH6lHF8WrjwKQ7uqVBM_EGWYTp-cFE1Uoug:1wVAf4:mHvFnyMzNeDD4pDl75woSqtRlwdHKgVfbjnR5cf3wAs','2026-06-18 16:11:14.316006'),('dbb65mohrbe83plga1tfkybve0on4v29','.eJxFizsKgDAMQK8imTuJUy_g6g0kthEC_ZE0k3h3q4vje7x3AcfOrZoaClfws4NS8yEUam6J-lCwMpZpYxJwI__T5UW1YKKYvpV0V2skGDMX8CcmpfsB_mUjYQ:1wV8f9:ahHf0UJ1zwaj1NfiyFE8_l_FqL3Hi-siYsACVVF1vv8','2026-06-18 14:03:11.282748'),('i3uwg7ze2ck6o8mc3hjqprmz0nla5vfv','.eJw9jDkOgDAMwL6CMneBkZUZ8QQUSoZI9FCOpYi_UxZGW7Jv4NO4FldH4QLzOAbIJR1CsaR6kXUHi7AaYx5WUsPccNjEuEHo9V9OH6lHF8WrjwKQ7uqVBM_EGWYTp-cFE1Uoug:1wVKRe:9KMMu10-Sky7ftaApXeGQ2khwaSE3FLxNfR_NSuLD3I','2026-06-19 02:38:02.363248'),('qwbpi7us8l808ie4u3koiusmyz6opqi0','eyJpZHRpcG91c3VhcmlvIjoxLCJub21icmVjb21wbGV0byI6IkNyaXN0aWFuIE1lc3RhbnphIE9ydGl6IiwiaWR1c3VhcmlvIjoyfQ:1wGgg1:qEcNAhQz3uqyoOWtRkj0v8xlpHTXfbZX03MkALlGbCg','2026-05-09 17:20:21.648136'),('rbodetcet1xb9v7i4ssfnwglm3ogtrxn','.eJw9y7EOgjAQANBfITcziFEQNwMrkcS4sJDD1ngBerW9YlL132Vyfcl7Aykhy8EHdMRwzFIwPA9O33i2k5aVoHLkhdAkjfaCJmJydkIR0jX_4zYFtNQLj9qsp_j4YFD6QQv2fLCndnk53da4VM-uDOq6m9jFsuqaPN7nYiM1PS6q2GdZPij4_gBuETXU:1w9QFd:qyCyGijJa3MsE8lWi5rZ4TVD2F4IqOvRvNOLbwv2a-M','2026-04-19 16:23:05.537941'),('u1fo7f4w8q6xjqjsqqlltkyhvjl86v1a','eyJpZHRpcG91c3VhcmlvIjoxLCJub21icmVjb21wbGV0byI6IkNyaXN0aWFuIE1lc3RhbnphIE9ydGl6IiwiaWR1c3VhcmlvIjoyfQ:1wEDzc:OqgTk68AzdnK03-iyymcfeUYm3UQhea5Tqik38OSG_g','2026-05-02 22:18:24.680932'),('v7u2v9sw4cez2xz733jqgzexh8wg4xb8','eyJpZHRpcG91c3VhcmlvIjoxLCJub21icmVjb21wbGV0byI6IkNyaXN0aWFuIE1lc3RhbnphIE9ydGl6IiwiaWR1c3VhcmlvIjoyfQ:1sSBdP:v1ZjVgqWLRhbl6veUnqmUo_0DTHCrnTr7H42r3jueeg','2024-07-26 08:28:07.567588');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleado` (
  `empleado_id` int NOT NULL AUTO_INCREMENT,
  `idempresa` int DEFAULT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `email` varchar(75) DEFAULT NULL,
  `telefono` varchar(9) DEFAULT NULL,
  `direccion` varchar(75) DEFAULT NULL,
  PRIMARY KEY (`empleado_id`),
  CONSTRAINT `empleado_ibfk_1` FOREIGN KEY (`empleado_id`) REFERENCES `empresa` (`idempresa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES `empleado` WRITE;
/*!40000 ALTER TABLE `empleado` DISABLE KEYS */;
/*!40000 ALTER TABLE `empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empresa`
--

DROP TABLE IF EXISTS `empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empresa` (
  `idempresa` int NOT NULL AUTO_INCREMENT,
  `ruc` varchar(11) NOT NULL,
  `razonsocial` varchar(255) NOT NULL,
  `nombrecomercial` varchar(255) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `mododev` int NOT NULL,
  `logo` varchar(255) NOT NULL,
  `telefono` varchar(25) NOT NULL,
  `usersec` varchar(255) NOT NULL,
  `passwordsec` varchar(255) NOT NULL,
  `ubigueo` varchar(10) DEFAULT NULL,
  `idsucursal` int DEFAULT NULL,
  `iddistrito` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`idempresa`),
  KEY `fk_sucursal_idx` (`idsucursal`),
  KEY `fk_distrito_idx` (`iddistrito`),
  CONSTRAINT `fk_distrito` FOREIGN KEY (`iddistrito`) REFERENCES `distritos` (`iddistrito`),
  CONSTRAINT `fk_sucursal` FOREIGN KEY (`idsucursal`) REFERENCES `sucursal` (`idsucursal`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresa`
--

LOCK TABLES `empresa` WRITE;
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
INSERT INTO `empresa` VALUES (1,'20615469751','Inversiones Peralta y Asociados SAC','Innovación Tecnológica','Jr. Augusto B. Leguia 484',1,'logos/logo_1.png','9167626762','PERA2015','Pera2015','220901',NULL,'220901');
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lotes`
--

DROP TABLE IF EXISTS `lotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lotes` (
  `idLote` int NOT NULL AUTO_INCREMENT,
  `idcompradetalle` int DEFAULT NULL,
  `idproducto` int DEFAULT NULL,
  `identificador` varchar(50) NOT NULL,
  `fecha_produccion` date DEFAULT NULL,
  `fecha_vencimiento` date DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  PRIMARY KEY (`idLote`),
  KEY `idcompradetalle` (`idcompradetalle`),
  KEY `idproducto` (`idproducto`),
  CONSTRAINT `lotes_ibfk_1` FOREIGN KEY (`idcompradetalle`) REFERENCES `compra_detalle` (`idcompradetalle`),
  CONSTRAINT `lotes_ibfk_2` FOREIGN KEY (`idproducto`) REFERENCES `producto` (`idproducto`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lotes`
--

LOCK TABLES `lotes` WRITE;
/*!40000 ALTER TABLE `lotes` DISABLE KEYS */;
INSERT INTO `lotes` VALUES (16,158,368,'1','2026-05-12','2026-06-06',2),(17,159,369,'2','2026-05-05','2026-06-06',2),(18,160,369,'1','2026-04-28','2026-06-06',2),(19,161,368,'2','2026-04-27','2026-06-05',3),(20,162,369,'1','2026-04-27','2026-06-06',2),(21,163,369,'00','2026-05-30','2026-05-30',3),(22,164,370,'11','2026-06-04','2026-06-11',1),(23,165,371,'222','2026-06-04','2026-06-11',3);
/*!40000 ALTER TABLE `lotes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modopago`
--

DROP TABLE IF EXISTS `modopago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modopago` (
  `idmodoPago` int NOT NULL AUTO_INCREMENT,
  `modo_pago` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idmodoPago`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modopago`
--

LOCK TABLES `modopago` WRITE;
/*!40000 ALTER TABLE `modopago` DISABLE KEYS */;
INSERT INTO `modopago` VALUES (1,'Efectivo'),(2,'Deposito'),(3,'Tarjeta crédito'),(4,'tarjeta débito'),(5,'Cheque'),(6,'Giro'),(7,'Otros');
/*!40000 ALTER TABLE `modopago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modulos`
--

DROP TABLE IF EXISTS `modulos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modulos` (
  `idmodulo` int NOT NULL AUTO_INCREMENT,
  `nombremodulo` varchar(255) NOT NULL,
  `estado` int NOT NULL DEFAULT '1',
  `url` varchar(45) DEFAULT NULL,
  `logo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idmodulo`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modulos`
--

LOCK TABLES `modulos` WRITE;
/*!40000 ALTER TABLE `modulos` DISABLE KEYS */;
INSERT INTO `modulos` VALUES (1,'Ventas',1,'/ventas','bi bi-cart'),(2,'Compras',1,'/compras','bi bi-bag'),(3,'Productos',1,'/productos','bi bi-basket3'),(5,'Usuarios',1,'/usuarios','bi bi-people'),(6,'Configuración',1,'/configuracion','bi bi-gear'),(7,'Unidades',1,'/unidades','bi bi-unity'),(8,'Permisos',1,'/permisos','bi bi-people'),(12,'Categorias',1,'/categorias','bi bi-bookmarks'),(13,'Cpanel',1,'/cpanel','fa-solid fa-chart-simple'),(14,'Tipo usuarios',1,'/tipousuarios','bi bi-people'),(15,'Número de seire',1,'/numeroserie','fas fa-list-ol'),(16,'Cerrar caja',1,'/cerrarcaja','fas fa-cash-register'),(17,'Ver caja',1,'/cajas','fas fa-cash-register'),(18,'Transacciones',1,'/transacciones','fas fa-credit-card'),(19,'Proveedores',1,'/proveedores','bi bi-truck'),(20,'Registro',1,NULL,NULL),(21,'Registro valorizado',1,NULL,NULL),(22,'Sucursales',1,NULL,NULL),(23,'Clientes',1,NULL,NULL),(24,'Cotizaciones',1,NULL,NULL);
/*!40000 ALTER TABLE `modulos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `numserie`
--

DROP TABLE IF EXISTS `numserie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `numserie` (
  `idnumserie` int NOT NULL AUTO_INCREMENT,
  `idtipodocumento` int NOT NULL,
  `numserie` varchar(4) DEFAULT NULL,
  `estado` int NOT NULL DEFAULT '1',
  `idsucursal` int DEFAULT NULL,
  PRIMARY KEY (`idnumserie`),
  KEY `idtipodocumento` (`idtipodocumento`),
  KEY `fk_numserie_sucursal_idx` (`idsucursal`),
  CONSTRAINT `fk_numserie_sucursal` FOREIGN KEY (`idsucursal`) REFERENCES `sucursal` (`idsucursal`),
  CONSTRAINT `numserie_ibfk_1` FOREIGN KEY (`idtipodocumento`) REFERENCES `tipodocumento` (`idtipodocumento`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `numserie`
--

LOCK TABLES `numserie` WRITE;
/*!40000 ALTER TABLE `numserie` DISABLE KEYS */;
INSERT INTO `numserie` VALUES (8,1,'F001',1,1),(9,3,'B001',1,1),(10,1,'F002',1,1),(11,3,'B002',1,1),(18,10,'NV01',1,1),(19,1,'F003',1,2),(20,3,'B003',1,2);
/*!40000 ALTER TABLE `numserie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `idproducto` int NOT NULL AUTO_INCREMENT,
  `idcategoria` int DEFAULT NULL,
  `nomproducto` varchar(255) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `precioCompra` double DEFAULT NULL,
  `preciounitario` double DEFAULT NULL,
  `stockactual` int DEFAULT NULL,
  `imagenprod` varchar(255) DEFAULT NULL,
  `estado` int DEFAULT '1',
  `codigo` varchar(45) DEFAULT NULL,
  `codigo_barras` varchar(45) DEFAULT NULL,
  `idunidad` int DEFAULT NULL,
  PRIMARY KEY (`idproducto`),
  KEY `idcategoria` (`idcategoria`),
  KEY `fk_unidad_idx` (`idunidad`),
  CONSTRAINT `fk_unidad` FOREIGN KEY (`idunidad`) REFERENCES `unidades` (`idunidad`),
  CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`idcategoria`) REFERENCES `categoria` (`idcategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=372 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (368,27,'Leche','leche',2,3,4,'',1,'000','000',1),(369,28,'Gaseosa','Gaseosa',1,2,5,'',1,'11','00',58),(370,27,'Yogur','Yogur',1,2,0,'',1,'11','00',58),(371,28,'Cifrut','Cifrut',1,2,8,'',1,'111','1111',58);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedores` (
  `idproveedor` int NOT NULL AUTO_INCREMENT,
  `idtipocliente` int NOT NULL,
  `numdoc` varchar(255) NOT NULL,
  `razonsocial` varchar(255) NOT NULL,
  `estado` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`idproveedor`),
  KEY `idtipocliente` (`idtipocliente`),
  CONSTRAINT `proveedores_ibfk_1` FOREIGN KEY (`idtipocliente`) REFERENCES `tipocliente` (`idtipocliente`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` VALUES (4,1,'10726558839','Cristian Mestanza Ortiz',1);
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provincias`
--

DROP TABLE IF EXISTS `provincias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provincias` (
  `idprovincia` varchar(11) NOT NULL,
  `nombreprovincia` varchar(255) NOT NULL,
  `iddepartamento` varchar(11) NOT NULL,
  PRIMARY KEY (`idprovincia`),
  KEY `fk_departamento_provincia` (`iddepartamento`),
  CONSTRAINT `fk_departamento_provincia` FOREIGN KEY (`iddepartamento`) REFERENCES `departamentos` (`iddepartamentos`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provincias`
--

LOCK TABLES `provincias` WRITE;
/*!40000 ALTER TABLE `provincias` DISABLE KEYS */;
INSERT INTO `provincias` VALUES ('0101','Chachapoyas','01'),('0102','Bagua','01'),('0103','Bongara','01'),('0104','Condorcanqui','01'),('0105','Luya','01'),('0106','Rodriguez de Mendoza','01'),('0107','Utcubamba','01'),('0201','Huaraz','02'),('0202','Aija','02'),('0203','Antonio Raymondi','02'),('0204','Asuncion','02'),('0205','Bolognesi','02'),('0206','Carhuaz','02'),('0207','Carlos Fermin Fitzca','02'),('0208','Casma','02'),('0209','Corongo','02'),('0210','Huari','02'),('0211','Huarmey','02'),('0212','Huaylas','02'),('0213','Mariscal Luzuriaga','02'),('0214','Ocros','02'),('0215','Pallasca','02'),('0216','Pomabamba','02'),('0217','Recuay','02'),('0218','Santa','02'),('0219','Sihuas','02'),('0220','Yungay','02'),('0301','Abancay','03'),('0302','Andahuaylas','03'),('0303','Antabamba','03'),('0304','Aymaraes','03'),('0305','Cotabambas','03'),('0306','Chincheros','03'),('0307','Grau','03'),('0401','Arequipa','04'),('0402','Camana','04'),('0403','Caraveli','04'),('0404','Castilla','04'),('0405','Caylloma','04'),('0406','Condesuyos','04'),('0407','Islay','04'),('0408','La Union','04'),('0501','Huamanga','05'),('0502','Cangallo','05'),('0503','Huanca Sancos','05'),('0504','Huanta','05'),('0505','La Mar','05'),('0506','Lucanas','05'),('0507','Parinacochas','05'),('0508','Paucar del Sara Sara','05'),('0509','Sucre','05'),('0510','Victor Fajardo','05'),('0511','Vilcas Huaman','05'),('0601','Cajamarca','06'),('0602','Cajabamba','06'),('0603','Celendin','06'),('0604','Chota','06'),('0605','Contumaza','06'),('0606','Cutervo','06'),('0607','Hualgayoc','06'),('0608','Jaen','06'),('0609','San Ignacio','06'),('0610','San Marcos','06'),('0611','San Miguel','06'),('0612','San Pablo','06'),('0613','Santa Cruz','06'),('0701','Callao','07'),('0801','Cusco','08'),('0802','Acomayo','08'),('0803','Anta','08'),('0804','Calca','08'),('0805','Canas','08'),('0806','Canchis','08'),('0807','Chumbivilcas','08'),('0808','Espinar','08'),('0809','La Convencion','08'),('0810','Paruro','08'),('0811','Paucartambo','08'),('0812','Quispicanchi','08'),('0813','Urubamba','08'),('0901','Huancavelica','09'),('0902','Acobamba','09'),('0903','Angaraes','09'),('0904','Castrovirreyna','09'),('0905','Churcampa','09'),('0906','Huaytara','09'),('0907','Tayacaja','09'),('1001','Huanuco','10'),('1002','Ambo','10'),('1003','Dos de Mayo','10'),('1004','Huacaybamba','10'),('1005','Huamalies','10'),('1006','Leoncio Prado','10'),('1007','Marañon','10'),('1008','Pachitea','10'),('1009','Puerto Inca','10'),('1010','Lauricocha','10'),('1011','Yarowilca','10'),('1101','Ica','11'),('1102','Chincha','11'),('1103','Nazca','11'),('1104','Palpa','11'),('1105','Pisco','11'),('1201','Huancayo','12'),('1202','Concepcion','12'),('1203','Chanchamayo','12'),('1204','Jauja','12'),('1205','Junin','12'),('1206','Satipo','12'),('1207','Tarma','12'),('1208','Yauli','12'),('1209','Chupaca','12'),('1301','Trujillo','13'),('1302','Ascope','13'),('1303','Bolivar','13'),('1304','Chepen','13'),('1305','Julcan','13'),('1306','Otuzco','13'),('1307','Pacasmayo','13'),('1308','Pataz','13'),('1309','Sanchez Carrion','13'),('1310','Santiago de Chuco','13'),('1311','Gran Chimu','13'),('1312','Viru','13'),('1401','Chiclayo','14'),('1402','Ferreñafe','14'),('1403','Lambayeque','14'),('1501','Lima','15'),('1502','Barranca','15'),('1503','Cajatambo','15'),('1504','Canta','15'),('1505','Cañete','15'),('1506','Huaral','15'),('1507','Huarochiri','15'),('1508','Huaura','15'),('1509','Oyon','15'),('1510','Yauyos','15'),('1601','Maynas','16'),('1602','Alto Amazonas','16'),('1603','Loreto','16'),('1604','Mariscal Ramon Castilla','16'),('1605','Requena','16'),('1606','Ucayali','16'),('1607','Datem del Marañon','16'),('1608','Putumayo','16'),('1701','Tambopata','17'),('1702','Manu','17'),('1703','Tahuamanu','17'),('1801','Mariscal Nieto','18'),('1802','General Sanchez Cerr','18'),('1803','Ilo','18'),('1901','Pasco','19'),('1902','Daniel Alcides Carri','19'),('1903','Oxapampa','19'),('2001','Piura','20'),('2002','Ayabaca','20'),('2003','Huancabamba','20'),('2004','Morropon','20'),('2005','Paita','20'),('2006','Sullana','20'),('2007','Talara','20'),('2008','Sechura','20'),('2101','Puno','21'),('2102','Azangaro','21'),('2103','Carabaya','21'),('2104','Chucuito','21'),('2105','El Collao','21'),('2106','Huancane','21'),('2107','Lampa','21'),('2108','Melgar','21'),('2109','Moho','21'),('2110','San Antonio de Putin','21'),('2111','San Roman','21'),('2112','Sandia','21'),('2113','Yunguyo','21'),('2201','Moyobamba','22'),('2202','Bellavista','22'),('2203','El Dorado','22'),('2204','Huallaga','22'),('2205','Lamas','22'),('2206','Mariscal Caceres','22'),('2207','Picota','22'),('2208','Rioja','22'),('2209','San Martin','22'),('2210','Tocache','22'),('2301','Tacna','23'),('2302','Candarave','23'),('2303','Jorge Basadre','23'),('2304','Tarata','23'),('2401','Tumbes','24'),('2402','Contralmirante Villa','24'),('2403','Zarumilla','24'),('2501','Coronel Portillo','25'),('2502','Atalaya','25'),('2503','Padre Abad','25'),('2504','Purus','25');
/*!40000 ALTER TABLE `provincias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sucursal`
--

DROP TABLE IF EXISTS `sucursal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sucursal` (
  `idsucursal` int NOT NULL AUTO_INCREMENT,
  `nombre_sursal` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`idsucursal`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sucursal`
--

LOCK TABLES `sucursal` WRITE;
/*!40000 ALTER TABLE `sucursal` DISABLE KEYS */;
INSERT INTO `sucursal` VALUES (1,'Casa Matriz'),(2,'Sucursal 2');
/*!40000 ALTER TABLE `sucursal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_entidad`
--

DROP TABLE IF EXISTS `tipo_entidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_entidad` (
  `id_tipo_entidad` int NOT NULL AUTO_INCREMENT,
  `tipo_entidad` varchar(45) DEFAULT NULL,
  `codigo` varchar(45) DEFAULT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  `abreviatura` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_tipo_entidad`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_entidad`
--

LOCK TABLES `tipo_entidad` WRITE;
/*!40000 ALTER TABLE `tipo_entidad` DISABLE KEYS */;
INSERT INTO `tipo_entidad` VALUES (1,'DNI','1','DOC.NACIONAL DE IDEN','DNI'),(2,'RUC','6','REG. UNICO DE CONTRI','RUC'),(3,'Empresas Del Extranjero - No Domiciliado','0','DOC.TRIB.NO.DOM.SIN.RUC','Emp. Ext'),(4,'Carnet de Extranjeria','4','CARNET DE EXTRANJERIA','Car. Ext'),(5,'Pasaporte','7','PASAPORTE','Pasaport'),(6,'Permiso Temporal de Permanencia - PTP','F','Permiso Temporal','PTP');
/*!40000 ALTER TABLE `tipo_entidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_igvs`
--

DROP TABLE IF EXISTS `tipo_igvs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_igvs` (
  `id_tipo_igv` int DEFAULT NULL,
  `codigo` int DEFAULT NULL,
  `tipo_igv` varchar(255) DEFAULT NULL,
  `codigo_de_tributo` int DEFAULT NULL,
  KEY `pk` (`id_tipo_igv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_igvs`
--

LOCK TABLES `tipo_igvs` WRITE;
/*!40000 ALTER TABLE `tipo_igvs` DISABLE KEYS */;
INSERT INTO `tipo_igvs` VALUES (1,10,'Gravado - Operación Onerosa',1000),(2,11,'Gravado - Retiro por premio',9996),(3,12,'Gravado - Retiro por donación',9996),(4,13,'Gravado - Retiro',9996),(5,14,'Gravado - Retiro por publicidad',9996),(6,15,'Gravado - Bonificaciones',9996),(7,16,'Gravado - Retiro por entrega a trabajadores',9996),(8,17,'Gravado - IVAP',9996),(9,20,'Exonerado - Operación Onerosa',9997),(10,21,'Exonerado - Transferencia gratuita',9996),(11,30,'Inafecto - Operación Onerosa',9998),(12,31,'Inafecto - Retiro por Bonificación',9996),(13,32,'Inafecto - Retiro',9996),(14,33,'Inafecto - Retiro por Muestras Médicas',9996),(15,34,'Inafecto - Retiro por Convenio Colectivo',9996),(16,35,'Inafecto - Retiro por premio',9996),(17,37,'Inafecto - Retiro por publicidad',9996),(18,14,'Inafecto - Transferencia gratuita',9996),(19,40,'Exportación de Bienes o Servicios',9995);
/*!40000 ALTER TABLE `tipo_igvs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_transaccion`
--

DROP TABLE IF EXISTS `tipo_transaccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_transaccion` (
  `id_tipo_transaccion` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(60) DEFAULT NULL,
  `ingresoegreso` int DEFAULT NULL,
  PRIMARY KEY (`id_tipo_transaccion`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_transaccion`
--

LOCK TABLES `tipo_transaccion` WRITE;
/*!40000 ALTER TABLE `tipo_transaccion` DISABLE KEYS */;
INSERT INTO `tipo_transaccion` VALUES (1,'Venta',1),(2,'Ingreso',1),(3,'Egreso',0),(4,'Compra',0);
/*!40000 ALTER TABLE `tipo_transaccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipocliente`
--

DROP TABLE IF EXISTS `tipocliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipocliente` (
  `idtipocliente` int NOT NULL AUTO_INCREMENT,
  `nomtipocliente` varchar(255) NOT NULL,
  `estado` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`idtipocliente`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipocliente`
--

LOCK TABLES `tipocliente` WRITE;
/*!40000 ALTER TABLE `tipocliente` DISABLE KEYS */;
INSERT INTO `tipocliente` VALUES (1,'Factura',1),(2,'Boleta',1),(3,'Nota de venta',1);
/*!40000 ALTER TABLE `tipocliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipodocumento`
--

DROP TABLE IF EXISTS `tipodocumento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipodocumento` (
  `idtipodocumento` int NOT NULL AUTO_INCREMENT,
  `codigosunat` varchar(10) NOT NULL,
  `nombredocumento` varchar(255) NOT NULL,
  `abrrdoc` varchar(10) NOT NULL,
  `estado` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`idtipodocumento`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipodocumento`
--

LOCK TABLES `tipodocumento` WRITE;
/*!40000 ALTER TABLE `tipodocumento` DISABLE KEYS */;
INSERT INTO `tipodocumento` VALUES (1,'01','Factura','F',1),(3,'03','Boleta','B',1),(7,'07','Nota de Credito','NC',0),(8,'08','Nota de Debito','ND',0),(9,'09','Guía de Remisión Remitente','GR',0),(10,'10','Nota de venta','NV',1);
/*!40000 ALTER TABLE `tipodocumento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipousuario`
--

DROP TABLE IF EXISTS `tipousuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipousuario` (
  `idtipousuario` int NOT NULL AUTO_INCREMENT,
  `nombretipousuario` varchar(255) NOT NULL,
  `estado` int NOT NULL DEFAULT '1',
  `es_superadmin` tinyint NOT NULL DEFAULT '0',
  PRIMARY KEY (`idtipousuario`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipousuario`
--

LOCK TABLES `tipousuario` WRITE;
/*!40000 ALTER TABLE `tipousuario` DISABLE KEYS */;
INSERT INTO `tipousuario` VALUES (1,'Administrador',1,0),(2,'Cajero',1,0),(3,'Mesero',1,0),(4,'Despecho222',0,0),(6,'Jijija',0,0),(7,'ss',0,0),(8,'dd',0,0),(9,'ss',0,0),(10,'ejemplo',1,0),(11,'Super Admin',1,1);
/*!40000 ALTER TABLE `tipousuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaccion`
--

DROP TABLE IF EXISTS `transaccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaccion` (
  `id_transaccion` int NOT NULL AUTO_INCREMENT,
  `id_caja` int DEFAULT NULL,
  `id_tipo_transaccion` int DEFAULT NULL,
  `monto` decimal(10,2) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  `idsucursal` int DEFAULT NULL,
  `idusuario` int DEFAULT NULL,
  PRIMARY KEY (`id_transaccion`),
  KEY `fk_caja_idx` (`id_caja`),
  KEY `fk_tipo_idx` (`id_tipo_transaccion`),
  KEY `fk_transaccion_sucursal_idx` (`idsucursal`),
  KEY `fk_transaccion_usuario_idx` (`idusuario`),
  CONSTRAINT `fk_caja` FOREIGN KEY (`id_caja`) REFERENCES `caja` (`id_caja`),
  CONSTRAINT `fk_tipo` FOREIGN KEY (`id_tipo_transaccion`) REFERENCES `tipo_transaccion` (`id_tipo_transaccion`),
  CONSTRAINT `fk_transaccion_sucursal` FOREIGN KEY (`idsucursal`) REFERENCES `sucursal` (`idsucursal`),
  CONSTRAINT `fk_transaccion_usuario` FOREIGN KEY (`idusuario`) REFERENCES `usuario` (`idusuario`)
) ENGINE=InnoDB AUTO_INCREMENT=135 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaccion`
--

LOCK TABLES `transaccion` WRITE;
/*!40000 ALTER TABLE `transaccion` DISABLE KEYS */;
INSERT INTO `transaccion` VALUES (121,24,1,2.00,'2026-05-29','17:06:51',NULL,1,NULL),(122,24,1,2.00,'2026-05-29','17:13:05',NULL,1,NULL),(123,24,1,2.00,'2026-05-29','17:21:29',NULL,1,NULL),(124,24,1,4.00,'2026-05-30','23:24:49',NULL,1,NULL),(125,24,1,2.36,'2026-06-04','09:02:36',NULL,1,NULL),(126,24,1,2.00,'2026-06-04','09:36:23',NULL,1,NULL),(127,24,1,2.00,'2026-06-04','09:40:53',NULL,1,NULL),(128,NULL,1,2.00,'2026-06-04','09:50:56',NULL,NULL,NULL),(129,NULL,1,2.00,'2026-06-04','09:50:58',NULL,NULL,NULL),(130,NULL,1,3.00,'2026-06-04','09:55:47',NULL,2,NULL),(131,NULL,1,2.36,'2026-06-04','09:59:59',NULL,2,24),(132,NULL,1,2.00,'2026-06-04','10:17:38',NULL,2,24),(133,24,1,5.00,'2026-06-04','21:37:45',NULL,1,2),(134,24,1,4.00,'2026-06-04','21:38:27',NULL,1,2);
/*!40000 ALTER TABLE `transaccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unidades`
--

DROP TABLE IF EXISTS `unidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unidades` (
  `idunidad` int NOT NULL AUTO_INCREMENT,
  `codigounidad` varchar(255) NOT NULL,
  `abrunidad` varchar(255) NOT NULL,
  `estado` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`idunidad`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unidades`
--

LOCK TABLES `unidades` WRITE;
/*!40000 ALTER TABLE `unidades` DISABLE KEYS */;
INSERT INTO `unidades` VALUES (1,'4A','BOBINAS',1),(2,'BJ','BALDE',1),(3,'BLL','BARRILES',1),(4,'BG','BOLSA',1),(5,'BO','BOTELLAS',1),(6,'BX','CAJA',1),(7,'CT','CARTONES',0),(8,'CMK','CENTIMETRO CUADRADO',0),(9,'CMQ','CENTIMETRO CUBICO',0),(10,'CMT','CENTIMETRO LINEAL',0),(11,'CEN','CIENTO DE UNIDADES',0),(12,'CY','CILINDRO',1),(13,'CJ','CONOS',0),(14,'DZN','DOCENA',0),(15,'DZP','DOCENA POR 10**6',0),(16,'BE','FARDO',0),(17,'GLI','GALON INGLES (4,545956L)',0),(18,'GRM','GRAMO',0),(19,'GRO','GRUESA',0),(20,'HLT','HECTOLITRO',0),(21,'LEF','HOJA',0),(22,'SET','JUEGO',0),(23,'KGM','KILOGRAMO',1),(24,'KTM','KILOMETRO',0),(25,'KWH','KILOVATIO HORA',0),(26,'KT','KIT',0),(27,'CA','LATAS',0),(28,'LBR','LIBRAS',0),(29,'LTR','LITRO',1),(30,'MWH','MEGAWATT HORA',0),(31,'MTR','METRO',1),(32,'MTK','METRO CUADRADO',0),(33,'MTQ','METRO CUBICO',0),(34,'MGM','MILIGRAMOS',0),(35,'MLT','MILILITRO',0),(36,'MMT','MILIMETRO',0),(37,'MMK','MILIMETRO CUADRADO',0),(38,'MMQ','MILIMETRO CUBICO',0),(39,'MLL','MILLARES',0),(40,'UM','MILLON DE UNIDADES',0),(41,'ONZ','ONZAS',0),(42,'PF','PALETAS',0),(43,'PK','PAQUETE',0),(44,'PR','PAR',0),(45,'FOT','PIES',0),(46,'FTK','PIES CUADRADOS',0),(47,'FTQ','PIES CUBICOS',0),(48,'C62','PIEZAS',0),(49,'PG','PLACAS',0),(50,'ST','PLIEGO',0),(51,'INH','PULGADAS',0),(52,'RM','RESMA',0),(53,'DR','TAMBOR',0),(54,'STN','TONELADA CORTA',0),(55,'LTN','TONELADA LARGA',0),(56,'TNE','TONELADAS',0),(57,'TU','TUBOS',0),(58,'NIU','UNIDAD (BIENES)',1),(59,'ZZ','UNIDAD (SERVICIOS)',1),(60,'GLL','US GALON (3,7843 L)',0),(61,'YRD','YARDA',0),(62,'YDK','YARDA CUADRADA',0),(63,'VA','VARIOS',0);
/*!40000 ALTER TABLE `unidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `idusuario` int NOT NULL AUTO_INCREMENT,
  `nombrecompleto` varchar(255) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `idtipousuario` int NOT NULL,
  `celular` varchar(10) NOT NULL,
  `dni` varchar(10) NOT NULL,
  `estado` int NOT NULL DEFAULT '1',
  `idsucursal` int DEFAULT NULL,
  PRIMARY KEY (`idusuario`),
  KEY `idtipousuario` (`idtipousuario`),
  KEY `fk_usuario_sucursal_idx` (`idsucursal`),
  CONSTRAINT `fk_usuario_sucursal` FOREIGN KEY (`idsucursal`) REFERENCES `sucursal` (`idsucursal`),
  CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`idtipousuario`) REFERENCES `tipousuario` (`idtipousuario`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (2,'Cristian Mestanza Ortiz','cristianmestanzaortiz870@gmail.com','1234',11,'916762676','72655883',1,1),(24,'Gian Pier','gian@gmail.com','1234',2,'916762676','72655883',1,2);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `idventa` int NOT NULL AUTO_INCREMENT,
  `idnumserie` int NOT NULL,
  `numcorrelativo` varchar(10) DEFAULT NULL,
  `idcliente` int DEFAULT NULL,
  `fechaemision` date DEFAULT NULL,
  `horaemision` time DEFAULT NULL,
  `estado` int DEFAULT NULL,
  `ruta_pdf` varchar(500) DEFAULT NULL,
  `ruta_ticket` varchar(500) DEFAULT NULL,
  `ruta_cdr` varchar(500) DEFAULT NULL,
  `respuesta_sunat_descripcion` varchar(500) DEFAULT NULL,
  `respuesta_sunat_codigo` varchar(500) DEFAULT NULL,
  `id_tipo_igv` int DEFAULT NULL,
  `idempresa` int DEFAULT NULL,
  `idmodoPago` int DEFAULT NULL,
  `total_gravada` float(10,2) DEFAULT NULL,
  `total_igv` float(10,2) DEFAULT NULL,
  `total_gratuita` decimal(10,2) DEFAULT NULL,
  `total_exonerada` decimal(10,2) DEFAULT NULL,
  `total_inafecta` decimal(10,2) DEFAULT NULL,
  `total_a_pagar` decimal(10,2) DEFAULT NULL,
  `api_id` int DEFAULT NULL,
  `ruta_xml` varchar(500) DEFAULT NULL,
  `detalle` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`idventa`),
  KEY `idnumserie` (`idnumserie`),
  KEY `idcliente` (`idcliente`),
  KEY `fk_igv_idx` (`id_tipo_igv`),
  KEY `fk_empresa_idx` (`idempresa`),
  KEY `fk_modoPago_idx` (`idmodoPago`),
  CONSTRAINT `fk` FOREIGN KEY (`id_tipo_igv`) REFERENCES `tipo_igvs` (`id_tipo_igv`),
  CONSTRAINT `fk_empresa` FOREIGN KEY (`idempresa`) REFERENCES `empresa` (`idempresa`),
  CONSTRAINT `fk_modoPago` FOREIGN KEY (`idmodoPago`) REFERENCES `modopago` (`idmodoPago`),
  CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`idnumserie`) REFERENCES `numserie` (`idnumserie`),
  CONSTRAINT `venta_ibfk_2` FOREIGN KEY (`idcliente`) REFERENCES `clientes` (`idcliente`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
INSERT INTO `venta` VALUES (44,9,'000001',220,'2026-05-29','17:06:50',0,'','/media/tickets/boletas/20615469751-03-B001-000001.pdf','','','',9,1,1,0.00,0.00,0.00,2.00,0.00,2.00,0,'','-'),(45,9,'000002',221,'2026-05-29','17:13:05',0,'','/media/tickets/boletas/20615469751-03-B001-000002.pdf','','','',9,1,1,0.00,0.00,0.00,2.00,0.00,2.00,0,'','-'),(46,9,'000003',222,'2026-05-29','17:21:29',1,'','/media/tickets/boletas/20615469751-03-B001-000003.pdf','','','',9,1,1,0.00,0.00,0.00,2.00,0.00,2.00,0,'','-'),(47,9,'000004',223,'2026-05-30','23:24:49',1,'','/media/tickets/boletas/20615469751-03-B001-000004.pdf','','','',9,1,1,0.00,0.00,0.00,4.00,0.00,4.00,0,'','-'),(48,20,'000001',224,'2026-06-04','09:02:36',1,'','/media/tickets/boletas/20615469751-03-B003-000001.pdf','','','',1,1,1,2.00,0.36,0.00,0.00,0.00,2.36,0,'','-'),(49,20,'000002',225,'2026-06-04','09:36:23',1,'','/media/tickets/boletas/20615469751-03-B003-000002.pdf','','','',9,1,1,0.00,0.00,0.00,2.00,0.00,2.00,0,'','-'),(50,9,'000005',226,'2026-06-04','09:40:53',1,'','/media/tickets/boletas/20615469751-03-B001-000005.pdf','','','',9,1,1,0.00,0.00,0.00,2.00,0.00,2.00,0,'','-'),(51,19,'000001',227,'2026-06-04','09:45:09',1,'','/media/tickets/facturas/20615469751-01-F003-000001.pdf','','','',9,1,1,0.00,0.00,0.00,3.00,0.00,3.00,0,'','-'),(52,20,'000003',228,'2026-06-04','09:50:56',1,'','/media/tickets/boletas/20615469751-03-B003-000003.pdf','','','',9,1,1,0.00,0.00,0.00,2.00,0.00,2.00,0,'','-'),(53,20,'000004',229,'2026-06-04','09:50:58',1,'','/media/tickets/boletas/20615469751-03-B003-000004.pdf','','','',9,1,1,0.00,0.00,0.00,2.00,0.00,2.00,0,'','-'),(54,20,'000005',230,'2026-06-04','09:55:47',1,'','/media/tickets/boletas/20615469751-03-B003-000005.pdf','','','',9,1,1,0.00,0.00,0.00,3.00,0.00,3.00,0,'','-'),(55,20,'000006',231,'2026-06-04','09:59:58',1,'','/media/tickets/boletas/20615469751-03-B003-000006.pdf','','','',1,1,1,2.00,0.36,0.00,0.00,0.00,2.36,0,'','-'),(56,20,'000007',220,'2026-06-04','10:17:37',1,'','/media/tickets/boletas/20615469751-03-B003-000007.pdf','','','',9,1,1,0.00,0.00,0.00,2.00,0.00,2.00,0,'','-'),(57,9,'000006',221,'2026-06-04','21:37:44',1,'','/media/tickets/boletas/20615469751-03-B001-000006.pdf','','','',9,1,1,0.00,0.00,0.00,5.00,0.00,5.00,0,'','-'),(58,9,'000007',221,'2026-06-04','21:38:27',1,'','/media/tickets/boletas/20615469751-03-B001-000007.pdf','','','',9,1,1,0.00,0.00,0.00,4.00,0.00,4.00,0,'','-');
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta_detalle`
--

DROP TABLE IF EXISTS `venta_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta_detalle` (
  `idventadetalle` int NOT NULL AUTO_INCREMENT,
  `idventa` int NOT NULL,
  `idproducto` int NOT NULL,
  `cantidad` decimal(10,2) NOT NULL,
  `preciosubtotal` decimal(10,2) NOT NULL,
  `detalle` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`idventadetalle`),
  KEY `idventa` (`idventa`),
  KEY `idproducto` (`idproducto`),
  CONSTRAINT `venta_detalle_ibfk_1` FOREIGN KEY (`idventa`) REFERENCES `venta` (`idventa`),
  CONSTRAINT `venta_detalle_ibfk_2` FOREIGN KEY (`idproducto`) REFERENCES `producto` (`idproducto`)
) ENGINE=InnoDB AUTO_INCREMENT=249 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta_detalle`
--

LOCK TABLES `venta_detalle` WRITE;
/*!40000 ALTER TABLE `venta_detalle` DISABLE KEYS */;
INSERT INTO `venta_detalle` VALUES (231,44,369,1.00,2.00,'-'),(232,45,369,1.00,2.00,'-'),(233,46,369,1.00,2.00,'-'),(234,47,369,1.00,2.00,'-'),(235,47,370,1.00,2.00,'-'),(236,48,370,1.00,2.00,'-'),(237,49,370,1.00,2.00,'-'),(238,50,369,1.00,2.00,'-'),(239,51,368,1.00,3.00,'-'),(240,52,370,1.00,2.00,'-'),(241,53,370,1.00,2.00,'-'),(242,54,368,1.00,3.00,'-'),(243,55,369,1.00,2.00,'-'),(244,56,369,1.00,2.00,'-'),(245,57,368,1.00,3.00,'-'),(246,57,369,1.00,2.00,'-'),(247,58,369,1.00,2.00,'-'),(248,58,370,1.00,2.00,'-');
/*!40000 ALTER TABLE `venta_detalle` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-04 22:34:26
