-- MySQL dump 10.17  Distrib 10.3.22-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: cliente
-- ------------------------------------------------------
-- Server version	10.3.22-MariaDB-1ubuntu1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clientes` (
  `nome_cliente` varchar(100) NOT NULL,
  `estado_civil_cliente` varchar(20) NOT NULL,
  `profissao_cliente` varchar(50) NOT NULL,
  `cpf_cliente` varchar(15) NOT NULL,
  `rg_cliente` varchar(10) NOT NULL,
  `rua_cliente` varchar(100) NOT NULL,
  `bairro_cliente` varchar(100) NOT NULL,
  `cidade_cliente` varchar(50) NOT NULL,
  `estado_cliente` varchar(50) NOT NULL,
  `cep_cliente` varchar(10) NOT NULL,
  `fone_cliente` varchar(20) NOT NULL,
  `nome_procurador` varchar(100) NOT NULL,
  `estado_civil_procurador` varchar(20) NOT NULL,
  `profissao_procurador` varchar(50) NOT NULL,
  `cpf_procurador` varchar(15) NOT NULL,
  `rg_procurador` varchar(10) NOT NULL,
  `rua_procurador` varchar(100) NOT NULL,
  `bairro_procurador` varchar(100) NOT NULL,
  `cidade_procurador` varchar(50) NOT NULL,
  `estado_procurador` varchar(50) NOT NULL,
  `cep_procurador` varchar(10) NOT NULL,
  `fone_procurador` varchar(20) NOT NULL,
  `motivo_procuracao` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES ('Andreza','solteiro(a)','estudante','888.888.888-88','8.888.888','do sol','sucupira','jaboatao','Pernambuco','55555-555','(55)5.5555-5555','andreia','casado(a)','dona de casa','454.444.444-44','4.444.444','do sol','sucupira','jaboatao','Pernambuco','55555-555','(55)5.5555-5555','somente para testar meu projetinho blz'),('Andreza','solteiro(a)','estudante','888.888.888-88','8.888.888','do sol','sucupira','jaboatao','Pernambuco','55555-555','(55)5.5555-5555','andreia','casado(a)','dona de casa','454.444.444-44','4.444.444','do sol','sucupira','jaboatao','Pernambuco','55555-555','(55)5.5555-5555','somente para testar meu projetinho blz'),('Andreza','solteiro(a)','estudante','888.888.888-88','8.888.888','do sol','sucupira','jaboatao','Pernambuco','55555-555','(55)5.5555-5555','andreia','casado(a)','dona de casa','454.444.444-44','4.444.444','do sol','sucupira','jaboatao','Pernambuco','55555-555','(55)5.5555-5555','somente para testar meu projetinho blz'),('Andreza','solteiro(a)','estudante','888.888.888-88','8.888.888','do sol','sucupira','jaboatao','Pernambuco','55555-555','(55)5.5555-5555','andreia','casado(a)','dona de casa','454.444.444-44','4.444.444','do sol','sucupira','jaboatao','Pernambuco','55555-555','(55)5.5555-5555','somente para testar meu projetinho blz');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-22 23:01:04
