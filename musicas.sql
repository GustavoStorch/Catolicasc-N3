-- MariaDB dump 10.19  Distrib 10.4.28-MariaDB, for Win64 (AMD64)
--
-- Host: 127.0.0.1    Database: musicas
-- ------------------------------------------------------
-- Server version	10.4.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `artistas`
--

DROP TABLE IF EXISTS `artistas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `artistas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `gravadoras_id` int(11) NOT NULL,
  `created` timestamp NULL DEFAULT NULL,
  `modified` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome_UNIQUE` (`nome`),
  KEY `fk_artistas_gravadoras1_idx` (`gravadoras_id`),
  CONSTRAINT `fk_artistas_gravadoras1` FOREIGN KEY (`gravadoras_id`) REFERENCES `gravadoras` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artistas`
--

LOCK TABLES `artistas` WRITE;
/*!40000 ALTER TABLE `artistas` DISABLE KEYS */;
INSERT INTO `artistas` VALUES (1,'Mano Lima',2,'2019-10-18 19:28:53','2019-10-18 19:28:53'),(2,'Shakira',4,'2019-10-18 19:29:46','2019-10-18 19:29:46'),(3,'Luiz Marenco',5,'2019-10-18 19:30:29','2019-10-18 19:30:29'),(4,'Pedro Capó',4,'2019-10-21 23:15:53','2019-10-21 23:15:53'),(5,'Farruko',4,'2019-10-21 23:16:19','2019-10-21 23:16:19'),(6,'Alicia Keys',4,'2019-10-21 23:16:28','2019-10-21 23:16:28'),(7,'Joca Martins',2,'2019-10-21 23:18:46','2019-10-21 23:18:46'),(8,'José Cláudio Machado',2,'2019-10-21 23:19:24','2019-10-21 23:19:24'),(9,'Luis Fonsi',4,'2019-10-21 23:23:42','2019-10-21 23:23:42'),(10,'Nicky Jam',4,'2019-10-21 23:25:48','2019-10-21 23:25:48'),(11,'Enrique Iglesias',4,'2019-10-21 23:45:55','2019-10-21 23:45:55'),(12,'Gente de Zona',4,'2019-10-21 23:46:07','2019-10-21 23:46:07'),(13,'Descemer Bueno',4,'2019-10-21 23:46:24','2019-10-21 23:46:24'),(14,'Zion',4,'2019-10-22 00:00:07','2019-10-22 00:00:07'),(15,'Lennox',4,'2019-10-22 00:00:16','2019-10-22 00:00:16'),(16,'Maluma',4,'2019-10-22 00:01:32','2019-10-22 00:01:32'),(17,'Anitta',4,'2019-10-22 00:01:43','2019-10-22 00:01:43'),(18,'Mettallica',4,'2019-10-22 00:02:34','2019-10-22 00:02:34'),(19,'MC Créu',1,'2019-10-22 00:22:44','2019-10-22 00:22:44'),(20,'Artista teste',1,NULL,NULL),(21,'Artista Atualizado',2,NULL,NULL);
/*!40000 ALTER TABLE `artistas` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER evitaAristasDuplicados
BEFORE INSERT ON artistas
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1
        FROM artistasView
        WHERE nome = NEW.nome
        AND gravadoras_id = NEW.gravadoras_id
    ) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Registro duplicado. Não é possível criar o artista.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER validaArtistasChaves
BEFORE INSERT ON artistas
FOR EACH ROW
BEGIN
    DECLARE count_rows INT;
    SELECT COUNT(id) INTO count_rows FROM gravadorasView WHERE id = NEW.gravadoras_id;
    IF count_rows = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Chave estrangeira inválida. Não é possível inserir o registro na tabela musicas.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary table structure for view `artistasview`
--

DROP TABLE IF EXISTS `artistasview`;
/*!50001 DROP VIEW IF EXISTS `artistasview`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `artistasview` AS SELECT
 1 AS `id`,
  1 AS `nome`,
  1 AS `gravadoras_id` */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(45) NOT NULL,
  `senha` varchar(45) NOT NULL,
  `created` timestamp NULL DEFAULT NULL,
  `modified` timestamp NULL DEFAULT NULL,
  `planos_id` int(11) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login_UNIQUE` (`login`),
  KEY `fk_usuarios_planos1_idx` (`planos_id`),
  CONSTRAINT `fk_usuarios_planos1` FOREIGN KEY (`planos_id`) REFERENCES `planos` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Sandro','5andr0','2019-10-18 19:08:20','2019-10-21 23:52:17',0,'sandrocamargo@unipampa.edu.br'),(2,'Papa','v5t1c5n0','2019-10-18 19:08:51','2019-10-21 23:52:42',3,'papa@vaticano.com'),(3,'Neymar','caicai','2019-10-21 23:14:56','2019-10-21 23:53:08',3,'bateu-caiu@selecao.com'),(4,'Cliente Teste','Teste',NULL,NULL,2,'cliente_teste@teste.com'),(5,'Cliente atualizado','atualizado',NULL,NULL,2,'cliente_atualizado@teste.com');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER evitaClientesDuplicados
BEFORE INSERT ON clientes
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1
        FROM clientesView
        WHERE login = NEW.login
        AND senha = NEW.senha
        AND planos_id = NEW.planos_id
        AND email = NEW.email
    ) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Registro duplicado. Não é possível criar o cliente.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER validaClientesChaves
BEFORE INSERT ON clientes
FOR EACH ROW
BEGIN
    DECLARE count_rows INT;
    SELECT COUNT(id) INTO count_rows FROM planosView WHERE id = NEW.planos_id;
    IF count_rows = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Chave estrangeira inválida. Não é possível inserir o registro na tabela cliente.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary table structure for view `clientesview`
--

DROP TABLE IF EXISTS `clientesview`;
/*!50001 DROP VIEW IF EXISTS `clientesview`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `clientesview` AS SELECT
 1 AS `id`,
  1 AS `login`,
  1 AS `senha`,
  1 AS `planos_id`,
  1 AS `email` */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `generos`
--

DROP TABLE IF EXISTS `generos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `generos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(45) NOT NULL,
  `created` timestamp NULL DEFAULT NULL,
  `modified` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `descricao_UNIQUE` (`descricao`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generos`
--

LOCK TABLES `generos` WRITE;
/*!40000 ALTER TABLE `generos` DISABLE KEYS */;
INSERT INTO `generos` VALUES (1,'Gaúcha','2019-10-18 19:10:38','2019-10-18 19:10:38'),(2,'Pop','2019-10-18 19:10:42','2019-10-18 19:10:42'),(3,'Rock','2019-10-18 19:10:46','2019-10-18 19:10:46'),(4,'Funk','2019-10-18 19:10:49','2019-10-18 19:10:49'),(5,'Genero de Teste',NULL,NULL),(6,'Genero atualizado',NULL,NULL);
/*!40000 ALTER TABLE `generos` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER evitaGenerosDuplicados
BEFORE INSERT ON generos
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1
        FROM generosView
        WHERE descricao = NEW.descricao
    ) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Registro duplicado. Não é possível criar o genero.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER deletarMusicasDoGenero
AFTER DELETE ON generos
FOR EACH ROW
BEGIN
    DELETE FROM musicas WHERE generos_id = OLD.id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER excluirMusicas AFTER DELETE ON generos
FOR EACH ROW
BEGIN
  DECLARE musicas_count INT;
  SELECT COUNT(*) INTO musicas_count FROM musicas WHERE generos_id = OLD.id;
  IF musicas_count = 0 THEN
    DELETE FROM musicas WHERE generos_id = OLD.id;
  END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary table structure for view `generosview`
--

DROP TABLE IF EXISTS `generosview`;
/*!50001 DROP VIEW IF EXISTS `generosview`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `generosview` AS SELECT
 1 AS `id`,
  1 AS `descricao` */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `gravadoras`
--

DROP TABLE IF EXISTS `gravadoras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gravadoras` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `valor_contrato` decimal(10,0) NOT NULL,
  `vencimento_contrato` date DEFAULT NULL,
  `created` timestamp NULL DEFAULT NULL,
  `modified` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome_UNIQUE` (`nome`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gravadoras`
--

LOCK TABLES `gravadoras` WRITE;
/*!40000 ALTER TABLE `gravadoras` DISABLE KEYS */;
INSERT INTO `gravadoras` VALUES (1,'Artista Independente',0,'2020-12-31','2019-10-18 19:18:32','2019-10-18 19:18:32'),(2,'ACIT',50000,'2020-12-31','2019-10-18 19:28:19','2019-10-18 19:28:19'),(3,'Som Livre',100000,'2020-12-31','2019-10-18 19:28:38','2019-10-18 19:28:38'),(4,'Sony Music',500000,'2024-12-31','2019-10-18 19:29:37','2019-10-18 19:29:37'),(5,'USA Discos',10000,'2020-12-31','2019-10-18 19:30:21','2019-10-18 19:30:21'),(6,'Gravadora de teste',100000,'2023-12-31',NULL,NULL),(7,'Nova gravadora de teste',80000,'2025-01-01',NULL,NULL);
/*!40000 ALTER TABLE `gravadoras` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER evitaGravadorasDuplicados
BEFORE INSERT ON gravadoras
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1
        FROM gravadorasView
        WHERE nome = NEW.nome
        AND valor_contrato = NEW.valor_contrato
        AND vencimento_contrato = NEW.vencimento_contrato
    ) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Registro duplicado. Não é possível criar a gravadora.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER atualizaGravadorasId
BEFORE DELETE ON gravadoras
FOR EACH ROW
BEGIN
    UPDATE artistas SET gravadoras_id = NULL WHERE gravadoras_id = OLD.id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary table structure for view `gravadorasview`
--

DROP TABLE IF EXISTS `gravadorasview`;
/*!50001 DROP VIEW IF EXISTS `gravadorasview`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `gravadorasview` AS SELECT
 1 AS `id`,
  1 AS `nome`,
  1 AS `valor_contrato`,
  1 AS `vencimento_contrato` */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `musicas`
--

DROP TABLE IF EXISTS `musicas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `musicas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `duracao` time NOT NULL,
  `generos_id` int(11) NOT NULL,
  `lancamento` date DEFAULT NULL,
  `created` timestamp NULL DEFAULT NULL,
  `modified` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_musicas_generos1_idx` (`generos_id`),
  CONSTRAINT `fk_musicas_generos1` FOREIGN KEY (`generos_id`) REFERENCES `generos` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `musicas`
--

LOCK TABLES `musicas` WRITE;
/*!40000 ALTER TABLE `musicas` DISABLE KEYS */;
INSERT INTO `musicas` VALUES (1,'Conta pro tio','04:00:00',1,'2014-01-01','2019-10-18 19:31:22','2019-10-18 19:31:22'),(2,'Balaio de gato','03:05:00',1,'2014-10-07','2019-10-21 18:06:51','2019-10-21 18:06:51'),(3,'Batendo água','15:09:00',1,'2014-02-06','2019-10-21 18:09:57','2019-10-21 18:09:57'),(4,'Estoy aqui','05:00:00',2,'2014-04-05','2019-10-21 18:18:10','2019-10-21 18:18:10'),(5,'Calma','20:15:00',2,'2018-12-31','2019-10-21 23:15:36','2019-10-21 23:15:36'),(6,'A boa vista do peão de tropa','04:18:00',1,'2014-12-31','2019-10-21 23:18:37','2019-10-21 23:18:37'),(7,'Espantando o Bagual','04:00:00',1,'2014-12-31','2019-10-21 23:21:20','2019-10-21 23:21:20'),(8,'Cadela Baia','03:59:00',1,'2014-12-31','2019-10-21 23:22:05','2019-10-21 23:22:05'),(9,'Sem paia e sem fumo','03:59:00',1,'2014-12-31','2019-10-21 23:22:52','2019-10-21 23:22:52'),(10,'Despacito','04:00:00',2,'2014-12-31','2019-10-21 23:23:30','2019-10-21 23:23:30'),(11,'Quando o verso vem pras casa','04:00:00',1,'2014-12-31','2019-10-21 23:24:28','2019-10-21 23:24:28'),(12,'Perro Fiel','03:59:00',2,'2014-12-31','2019-10-21 23:26:15','2019-10-21 23:26:15'),(13,'Bailando','04:00:00',2,'2014-12-31','2019-10-21 23:46:59','2019-10-21 23:46:59'),(14,'El perdón','03:54:00',2,'2014-12-31','2019-10-21 23:54:37','2019-10-21 23:54:37'),(15,'Súbeme la Radio','03:30:00',2,'2014-12-31','2019-10-22 00:00:39','2019-10-22 00:00:39'),(16,'Sim ou Não','04:00:00',2,'2014-12-31','2019-10-22 00:00:48','2019-10-22 00:02:16'),(17,'Felices los 4','03:59:00',2,'2014-12-31','2019-10-22 00:21:54','2019-10-22 00:21:54'),(18,'Dança do Créu','01:59:00',4,'2014-12-31','2019-10-22 00:22:59','2019-10-22 00:22:59'),(20,'Cedo ou Tarde','03:13:00',3,'2015-06-06',NULL,NULL),(21,'Música Teste','03:45:00',1,'2023-06-21',NULL,NULL),(22,'Música Atualizada','03:15:00',1,'2023-06-21',NULL,NULL);
/*!40000 ALTER TABLE `musicas` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER evitaMusicasDuplicados
BEFORE INSERT ON musicas
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1
        FROM musicasView
        WHERE nome = NEW.nome
        AND duracao = NEW.duracao
        AND generos_id = NEW.generos_id
        AND lancamento = NEW.lancamento
    ) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Registro duplicado. Não é possível criar a musica.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER validaMusicasChaves
BEFORE INSERT ON musicas
FOR EACH ROW
BEGIN
    DECLARE count_rows INT;
    SELECT COUNT(id) INTO count_rows FROM generosView WHERE id = NEW.generos_id;
    IF count_rows = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Chave estrangeira inválida. Não é possível inserir o registro na tabela musicas.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `musicas_has_artistas`
--

DROP TABLE IF EXISTS `musicas_has_artistas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `musicas_has_artistas` (
  `id` int(11) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `musicas_id` int(11) NOT NULL,
  `artistas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_musicas_has_artistas_artistas1_idx` (`artistas_id`),
  KEY `fk_musicas_has_artistas_musicas1_idx` (`musicas_id`),
  KEY `id` (`id`),
  CONSTRAINT `fk_musicas_has_artistas_artistas1` FOREIGN KEY (`artistas_id`) REFERENCES `artistas` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_musicas_has_artistas_musicas1` FOREIGN KEY (`musicas_id`) REFERENCES `musicas` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `musicas_has_artistas`
--

LOCK TABLES `musicas_has_artistas` WRITE;
/*!40000 ALTER TABLE `musicas_has_artistas` DISABLE KEYS */;
INSERT INTO `musicas_has_artistas` VALUES (00000000002,2,1),(00000000003,3,3),(00000000004,4,2),(00000000005,5,4),(00000000006,5,5),(00000000007,5,6),(00000000008,6,8),(00000000009,6,7),(00000000010,6,3),(00000000011,7,1),(00000000012,8,1),(00000000013,9,1),(00000000014,10,9),(00000000015,11,3),(00000000016,12,2),(00000000017,12,10),(00000000018,13,13),(00000000019,13,11),(00000000020,13,12),(00000000021,14,11),(00000000022,14,10),(00000000023,16,17),(00000000024,16,16),(00000000025,15,11),(00000000026,15,15),(00000000027,15,14),(00000000028,15,13),(00000000029,17,16),(00000000030,18,19);
/*!40000 ALTER TABLE `musicas_has_artistas` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER evitaMusicaHasArtistaDuplicados
BEFORE INSERT ON musicas_has_artistas
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1
        FROM musicasHasArtistasView
        WHERE musicas_id = NEW.musicas_id
        AND artistas_id = NEW.artistas_id
    ) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Registro duplicado. Não é possível criar o registro';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER validaMusicasHasArtistasChaves
BEFORE INSERT ON musicas_has_artistas
FOR EACH ROW
BEGIN
    DECLARE count_musicas INT;
    DECLARE count_artistas INT;
    
    SELECT COUNT(*) INTO count_musicas FROM musicas WHERE id = NEW.musicas_id;
    SELECT COUNT(*) INTO count_artistas FROM artistas WHERE id = NEW.artistas_id;
    
    IF count_musicas = 0 OR count_artistas = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Chave estrangeira inválida. Não é possível inserir o registro na tabela musicas_has_artistas.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `musicas_has_clientes`
--

DROP TABLE IF EXISTS `musicas_has_clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `musicas_has_clientes` (
  `id` int(11) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `musicas_id` int(11) NOT NULL,
  `clientes_id` int(11) NOT NULL,
  `data` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_musicas_has_usuarios_musicas1_idx` (`musicas_id`),
  KEY `fk_musicas_has_usuarios_clientes1_idx` (`clientes_id`),
  CONSTRAINT `fk_musicas_has_usuarios_clientes1` FOREIGN KEY (`clientes_id`) REFERENCES `clientes` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_musicas_has_usuarios_musicas1` FOREIGN KEY (`musicas_id`) REFERENCES `musicas` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=12121214 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `musicas_has_clientes`
--

LOCK TABLES `musicas_has_clientes` WRITE;
/*!40000 ALTER TABLE `musicas_has_clientes` DISABLE KEYS */;
INSERT INTO `musicas_has_clientes` VALUES (00000000001,4,1,'2019-10-21 18:19:00'),(00000000002,1,1,'2019-10-22 00:28:00'),(00000000003,1,1,'2019-10-22 00:29:00');
/*!40000 ALTER TABLE `musicas_has_clientes` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER evitaMusicaHasClienteDuplicados
BEFORE INSERT ON musicas_has_clientes
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1
        FROM musicasHasClientesView
        WHERE musicas_id = NEW.musicas_id
        AND clientes_id = NEW.clientes_id
    ) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Registro duplicado. Não é possível criar o registro';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary table structure for view `musicashasartistasview`
--

DROP TABLE IF EXISTS `musicashasartistasview`;
/*!50001 DROP VIEW IF EXISTS `musicashasartistasview`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `musicashasartistasview` AS SELECT
 1 AS `id`,
  1 AS `musicas_id`,
  1 AS `artistas_id` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `musicashasclientesview`
--

DROP TABLE IF EXISTS `musicashasclientesview`;
/*!50001 DROP VIEW IF EXISTS `musicashasclientesview`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `musicashasclientesview` AS SELECT
 1 AS `id`,
  1 AS `musicas_id`,
  1 AS `clientes_id`,
  1 AS `data` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `musicasview`
--

DROP TABLE IF EXISTS `musicasview`;
/*!50001 DROP VIEW IF EXISTS `musicasview`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `musicasview` AS SELECT
 1 AS `id`,
  1 AS `nome`,
  1 AS `duracao`,
  1 AS `generos_id`,
  1 AS `lancamento` */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `pagamentos`
--

DROP TABLE IF EXISTS `pagamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pagamentos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagamentos`
--

LOCK TABLES `pagamentos` WRITE;
/*!40000 ALTER TABLE `pagamentos` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagamentos` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER evitaPagamentosDuplicados
BEFORE INSERT ON pagamentos
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1
        FROM pagamentosView
        WHERE data = NEW.data
    ) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Registro duplicado. Não é possível criar o pagamento.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary table structure for view `pagamentosview`
--

DROP TABLE IF EXISTS `pagamentosview`;
/*!50001 DROP VIEW IF EXISTS `pagamentosview`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `pagamentosview` AS SELECT
 1 AS `id`,
  1 AS `data` */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `planos`
--

DROP TABLE IF EXISTS `planos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `planos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(45) NOT NULL,
  `valor` decimal(5,2) NOT NULL,
  `limite` int(11) NOT NULL,
  `created` timestamp NULL DEFAULT NULL,
  `modified` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `descricao_UNIQUE` (`descricao`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `planos`
--

LOCK TABLES `planos` WRITE;
/*!40000 ALTER TABLE `planos` DISABLE KEYS */;
INSERT INTO `planos` VALUES (2,'Sem nome',39.99,500,'2019-10-18 17:21:31','2019-10-18 17:21:31'),(3,'Full',49.99,999999,'2019-10-18 17:22:00','2019-10-18 17:22:00'),(7,'Premium',56.99,999,NULL,NULL),(8,'Plano de teste',10.99,100,NULL,NULL),(9,'Novo plano de teste',15.00,200,NULL,NULL);
/*!40000 ALTER TABLE `planos` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER evitaPlanosDuplicados
BEFORE INSERT ON planos
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1
        FROM planosView
        WHERE descricao = NEW.descricao
            AND valor = NEW.valor
            AND limite = NEW.limite
    ) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Registro duplicado. Não é possível criar o plano.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER atualizaPlanosId
BEFORE DELETE ON planos
FOR EACH ROW
BEGIN
    UPDATE clientes SET planos_id = NULL WHERE planos_id = OLD.id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary table structure for view `planosview`
--

DROP TABLE IF EXISTS `planosview`;
/*!50001 DROP VIEW IF EXISTS `planosview`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `planosview` AS SELECT
 1 AS `id`,
  1 AS `descricao`,
  1 AS `valor`,
  1 AS `limite` */;
SET character_set_client = @saved_cs_client;

--
-- Dumping events for database 'musicas'
--

--
-- Dumping routines for database 'musicas'
--

--
-- Final view structure for view `artistasview`
--

/*!50001 DROP VIEW IF EXISTS `artistasview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `artistasview` AS select `artistas`.`id` AS `id`,`artistas`.`nome` AS `nome`,`artistas`.`gravadoras_id` AS `gravadoras_id` from `artistas` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `clientesview`
--

/*!50001 DROP VIEW IF EXISTS `clientesview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `clientesview` AS select `clientes`.`id` AS `id`,`clientes`.`login` AS `login`,`clientes`.`senha` AS `senha`,`clientes`.`planos_id` AS `planos_id`,`clientes`.`email` AS `email` from `clientes` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `generosview`
--

/*!50001 DROP VIEW IF EXISTS `generosview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `generosview` AS select `generos`.`id` AS `id`,`generos`.`descricao` AS `descricao` from `generos` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `gravadorasview`
--

/*!50001 DROP VIEW IF EXISTS `gravadorasview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `gravadorasview` AS select `gravadoras`.`id` AS `id`,`gravadoras`.`nome` AS `nome`,`gravadoras`.`valor_contrato` AS `valor_contrato`,`gravadoras`.`vencimento_contrato` AS `vencimento_contrato` from `gravadoras` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `musicashasartistasview`
--

/*!50001 DROP VIEW IF EXISTS `musicashasartistasview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `musicashasartistasview` AS select `musicas_has_artistas`.`id` AS `id`,`musicas_has_artistas`.`musicas_id` AS `musicas_id`,`musicas_has_artistas`.`artistas_id` AS `artistas_id` from `musicas_has_artistas` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `musicashasclientesview`
--

/*!50001 DROP VIEW IF EXISTS `musicashasclientesview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `musicashasclientesview` AS select `musicas_has_clientes`.`id` AS `id`,`musicas_has_clientes`.`musicas_id` AS `musicas_id`,`musicas_has_clientes`.`clientes_id` AS `clientes_id`,`musicas_has_clientes`.`data` AS `data` from `musicas_has_clientes` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `musicasview`
--

/*!50001 DROP VIEW IF EXISTS `musicasview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `musicasview` AS select `musicas`.`id` AS `id`,`musicas`.`nome` AS `nome`,`musicas`.`duracao` AS `duracao`,`musicas`.`generos_id` AS `generos_id`,`musicas`.`lancamento` AS `lancamento` from `musicas` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `pagamentosview`
--

/*!50001 DROP VIEW IF EXISTS `pagamentosview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `pagamentosview` AS select `pagamentos`.`id` AS `id`,`pagamentos`.`data` AS `data` from `pagamentos` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `planosview`
--

/*!50001 DROP VIEW IF EXISTS `planosview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `planosview` AS select `planos`.`id` AS `id`,`planos`.`descricao` AS `descricao`,`planos`.`valor` AS `valor`,`planos`.`limite` AS `limite` from `planos` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-23 17:53:44
