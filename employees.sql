-- MySQL dump 10.13  Distrib 8.0.43, for macos15 (arm64)
--
-- Host: 127.0.0.1    Database: cselect
-- ------------------------------------------------------
-- Server version	9.4.0

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
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `age` tinyint DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'John','Doe',28,'New York'),(2,'Jane','Smith',32,'Los Angeles'),(3,'Michael','Brown',26,'Chicago'),(4,'Emily','Davis',30,'Houston'),(5,'Daniel','Miller',27,'Phoenix'),(6,'Sophia','Wilson',25,'Philadelphia'),(7,'James','Taylor',35,'San Antonio'),(8,'Olivia','Martinez',29,'San Diego'),(9,'William','Anderson',31,'Dallas'),(10,'Ava','Thomas',24,'San Jose'),(11,'Benjamin','Jackson',33,'Austin'),(12,'Mia','White',22,'Fort Worth'),(13,'Alexander','Harris',29,'Columbus'),(14,'Isabella','Clark',28,'Charlotte'),(15,'Ethan','Lewis',27,'San Francisco'),(16,'Amelia','Robinson',26,'Indianapolis'),(17,'Logan','Walker',34,'Seattle'),(18,'Harper','Perez',23,'Denver'),(19,'Jacob','Hall',30,'Washington'),(20,'Ella','Young',21,'Boston');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store`
--

DROP TABLE IF EXISTS `store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store` (
  `id` int NOT NULL AUTO_INCREMENT,
  `store_name` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `store_hours` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store`
--

LOCK TABLES `store` WRITE;
/*!40000 ALTER TABLE `store` DISABLE KEYS */;
INSERT INTO `store` VALUES (1,'FreshMart','New York','8:00 AM - 9:00 PM'),(2,'City Grocers','Los Angeles','9:00 AM - 10:00 PM'),(3,'TechHub','Chicago','10:00 AM - 8:00 PM'),(4,'Home Essentials','Houston','8:30 AM - 9:30 PM'),(5,'BookWorld','Phoenix','9:00 AM - 7:00 PM'),(6,'Daily Needs','San Antonio','7:00 AM - 9:00 PM'),(7,'MegaStore','San Diego','24 Hours'),(8,'Fashion Lane','Dallas','10:00 AM - 9:00 PM'),(9,'Gadget House','San Jose','9:30 AM - 8:30 PM'),(10,'EcoShop','Austin','8:00 AM - 8:00 PM'),(11,'Pet Paradise','Jacksonville','9:00 AM - 9:00 PM'),(12,'Beauty Corner','Fort Worth','10:00 AM - 7:00 PM'),(13,'Toy Galaxy','Columbus','9:00 AM - 8:00 PM'),(14,'Green Pharmacy','Charlotte','24 Hours'),(15,'Kitchen Pro','San Francisco','10:00 AM - 10:00 PM'),(16,'Sport Zone','Indianapolis','9:00 AM - 9:00 PM'),(17,'Music Hub','Seattle','10:00 AM - 9:00 PM'),(18,'Healthy Life','Denver','8:00 AM - 9:00 PM'),(19,'Snack Shop','Washington','7:30 AM - 10:00 PM'),(20,'Bargain Depot','Boston','8:00 AM - 11:00 PM');
/*!40000 ALTER TABLE `store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `supplier_id` int NOT NULL AUTO_INCREMENT,
  `supplier_name` varchar(70) NOT NULL,
  `contact_number` int DEFAULT NULL,
  `store_id` int DEFAULT NULL,
  PRIMARY KEY (`supplier_id`),
  KEY `store_id` (`store_id`),
  CONSTRAINT `supplier_ibfk_1` FOREIGN KEY (`store_id`) REFERENCES `store` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'Fresh Supply Co.',917123450,1),(2,'City Distributors',918234560,2),(3,'Tech Parts Inc.',919345670,3),(4,'Home Goods Trading',920456780,4),(5,'BookLink Corp.',921567890,5),(6,'Daily Needs Supply',922678901,6),(7,'Mega Retail Suppliers',923789012,7),(8,'Fashion Traders',924890123,8),(9,'Gadget Hub Trading',925901234,9),(10,'EcoPackage Ltd.',926012345,10),(11,'Pet Essentials PH',927123451,11),(12,'BeautyChain Inc.',928234572,12),(13,'Toy Kingdom Supply',929346783,13),(14,'GreenMedical Traders',930567894,14),(15,'KitchenWorks Co.',931568905,15),(16,'Sporting Supply PH',932689016,16),(17,'MusicTone Suppliers',937890127,17),(18,'Health & Care Dist.',934901238,18),(19,'Snack Central Dist.',939012349,19),(20,'Bargain Lot Traders',930123450,20);
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-12 23:00:02
