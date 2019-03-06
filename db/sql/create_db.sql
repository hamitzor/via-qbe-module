-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 06, 2019 at 09:49 AM
-- Server version: 5.7.25-0ubuntu0.18.04.2
-- PHP Version: 7.2.15-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `via`
--

-- --------------------------------------------------------

--
-- Table structure for table `Anomalies`
--

CREATE TABLE `Anomalies` (
  `AnomalyId` int(11) NOT NULL,
  `RelatedFunctionName` varchar(64) NOT NULL,
  `Description` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `DetectedAnomalies`
--

CREATE TABLE `DetectedAnomalies` (
  `DetectedAnomalyId` int(11) NOT NULL,
  `OrderId` int(11) NOT NULL,
  `RuleId` int(11) NOT NULL,
  `FrameNo` int(11) NOT NULL,
  `DetectedTime` datetime NOT NULL,
  `InterestObjects` int(11) NOT NULL,
  `InterestPosition` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `DetectedObjects`
--

CREATE TABLE `DetectedObjects` (
  `DetectedObjectId` int(11) NOT NULL,
  `ObjectId` int(11) NOT NULL,
  `FrameNo` int(11) NOT NULL,
  `TopLeft` int(4) NOT NULL,
  `BottomRight` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Objects`
--

CREATE TABLE `Objects` (
  `ObjectId` int(11) NOT NULL,
  `Label` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `RuleAnomaly`
--

CREATE TABLE `RuleAnomaly` (
  `RuleAnomalyId` int(11) NOT NULL,
  `RuleId` int(11) NOT NULL,
  `AnomalyId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Rules`
--

CREATE TABLE `Rules` (
  `RuleId` int(11) NOT NULL,
  `RuleDescription` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `UserId` int(11) NOT NULL,
  `Email` varchar(64) NOT NULL,
  `RegistrationDate` datetime NOT NULL,
  `FirstName` varchar(64) DEFAULT NULL,
  `LastName` varchar(64) DEFAULT NULL,
  `Password` varchar(256) NOT NULL,
  `LastPasswordChangeDate` datetime NOT NULL,
  `NotificationAnomaly` tinyint(4) NOT NULL,
  `StorageUsedSize` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `VideoDetectedAnomaly`
--

CREATE TABLE `VideoDetectedAnomaly` (
  `VideoDetectedAnomalyId` int(11) NOT NULL,
  `DetectedAnomalyId` int(11) NOT NULL,
  `VideoId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `VideoDetectedObject`
--

CREATE TABLE `VideoDetectedObject` (
  `VideoDetectedObjectId` int(11) NOT NULL,
  `DetectedObjectId` int(11) NOT NULL,
  `VideoId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `VideoFeatures`
--

CREATE TABLE `VideoFeatures` (
  `VideoFeatureId` int(11) NOT NULL,
  `FrameNo` int(11) NOT NULL,
  `KeypointAngle` float DEFAULT NULL,
  `KeypointOctave` int(11) DEFAULT NULL,
  `KeypointPtX` int(11) NOT NULL,
  `KeypointPtY` int(11) NOT NULL,
  `KeypointResponse` float DEFAULT NULL,
  `KeypointSize` float DEFAULT NULL,
  `Descriptor` varchar(512) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Videos`
--

CREATE TABLE `Videos` (
  `VideoId` int(11) NOT NULL,
  `CreationDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Title` varchar(256) NOT NULL,
  `Length` int(11) NOT NULL,
  `FileFormat` varchar(64) NOT NULL,
  `FileName` varchar(256) NOT NULL,
  `FileSize` int(11) NOT NULL,
  `FilePath` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Videos`
--

INSERT INTO `Videos` (`VideoId`, `CreationDate`, `Title`, `Length`, `FileFormat`, `FileName`, `FileSize`, `FilePath`) VALUES
(1, '2019-03-04 04:55:43', 'Demo', 60, 'mp4', 'demo.mp4', 8305, '/home/hamit/via/media_source/video/demo.mp4');

-- --------------------------------------------------------

--
-- Table structure for table `VideoUser`
--

CREATE TABLE `VideoUser` (
  `VideoUserId` int(11) NOT NULL,
  `UserId` int(11) NOT NULL,
  `VideoId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `VideoVideoFeature`
--

CREATE TABLE `VideoVideoFeature` (
  `VideoVideoFeatureId` int(11) NOT NULL,
  `VideoFeatureId` int(11) NOT NULL,
  `VideoId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Anomalies`
--
ALTER TABLE `Anomalies`
  ADD PRIMARY KEY (`AnomalyId`);

--
-- Indexes for table `DetectedAnomalies`
--
ALTER TABLE `DetectedAnomalies`
  ADD PRIMARY KEY (`DetectedAnomalyId`),
  ADD KEY `FK_DetectedAnomalies_Rules` (`RuleId`);

--
-- Indexes for table `DetectedObjects`
--
ALTER TABLE `DetectedObjects`
  ADD PRIMARY KEY (`DetectedObjectId`),
  ADD KEY `FK_DetectedObjects_Objects` (`ObjectId`);

--
-- Indexes for table `Objects`
--
ALTER TABLE `Objects`
  ADD PRIMARY KEY (`ObjectId`);

--
-- Indexes for table `RuleAnomaly`
--
ALTER TABLE `RuleAnomaly`
  ADD PRIMARY KEY (`RuleAnomalyId`),
  ADD KEY `FK_RuleAnomaly_Rule` (`RuleId`),
  ADD KEY `FK_RuleAnomaly_Anomaly` (`AnomalyId`);

--
-- Indexes for table `Rules`
--
ALTER TABLE `Rules`
  ADD PRIMARY KEY (`RuleId`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`UserId`);

--
-- Indexes for table `VideoDetectedAnomaly`
--
ALTER TABLE `VideoDetectedAnomaly`
  ADD PRIMARY KEY (`VideoDetectedAnomalyId`),
  ADD KEY `FK_VideoDetectedAnomaly_DetectedAnomalies` (`DetectedAnomalyId`),
  ADD KEY `FK_VideoDetectedAnomaly_Videos` (`VideoId`);

--
-- Indexes for table `VideoDetectedObject`
--
ALTER TABLE `VideoDetectedObject`
  ADD PRIMARY KEY (`VideoDetectedObjectId`),
  ADD KEY `FK_VideoDetectedObjecst_DetectedObjects` (`DetectedObjectId`),
  ADD KEY `FK_VideoDetectedObjecst_Videos` (`VideoId`);

--
-- Indexes for table `VideoFeatures`
--
ALTER TABLE `VideoFeatures`
  ADD PRIMARY KEY (`VideoFeatureId`);

--
-- Indexes for table `Videos`
--
ALTER TABLE `Videos`
  ADD PRIMARY KEY (`VideoId`);

--
-- Indexes for table `VideoUser`
--
ALTER TABLE `VideoUser`
  ADD PRIMARY KEY (`VideoUserId`),
  ADD KEY `FK_VideoUser_Videos` (`VideoId`),
  ADD KEY `FK_VideoUser_Users` (`UserId`);

--
-- Indexes for table `VideoVideoFeature`
--
ALTER TABLE `VideoVideoFeature`
  ADD PRIMARY KEY (`VideoVideoFeatureId`),
  ADD KEY `FK_VideoVideoFeature_Videos` (`VideoId`),
  ADD KEY `FK_VideoVideoFeature_VideoFeatures` (`VideoFeatureId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Anomalies`
--
ALTER TABLE `Anomalies`
  MODIFY `AnomalyId` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `DetectedAnomalies`
--
ALTER TABLE `DetectedAnomalies`
  MODIFY `DetectedAnomalyId` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `DetectedObjects`
--
ALTER TABLE `DetectedObjects`
  MODIFY `DetectedObjectId` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Objects`
--
ALTER TABLE `Objects`
  MODIFY `ObjectId` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `RuleAnomaly`
--
ALTER TABLE `RuleAnomaly`
  MODIFY `RuleAnomalyId` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Rules`
--
ALTER TABLE `Rules`
  MODIFY `RuleId` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `UserId` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `VideoDetectedAnomaly`
--
ALTER TABLE `VideoDetectedAnomaly`
  MODIFY `VideoDetectedAnomalyId` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `VideoDetectedObject`
--
ALTER TABLE `VideoDetectedObject`
  MODIFY `VideoDetectedObjectId` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `VideoFeatures`
--
ALTER TABLE `VideoFeatures`
  MODIFY `VideoFeatureId` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Videos`
--
ALTER TABLE `Videos`
  MODIFY `VideoId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `VideoUser`
--
ALTER TABLE `VideoUser`
  MODIFY `VideoUserId` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `VideoVideoFeature`
--
ALTER TABLE `VideoVideoFeature`
  MODIFY `VideoVideoFeatureId` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `DetectedAnomalies`
--
ALTER TABLE `DetectedAnomalies`
  ADD CONSTRAINT `FK_DetectedAnomalies_Rules` FOREIGN KEY (`RuleId`) REFERENCES `Rules` (`RuleId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `DetectedObjects`
--
ALTER TABLE `DetectedObjects`
  ADD CONSTRAINT `FK_DetectedObjects_Objects` FOREIGN KEY (`ObjectId`) REFERENCES `Objects` (`ObjectId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `RuleAnomaly`
--
ALTER TABLE `RuleAnomaly`
  ADD CONSTRAINT `FK_RuleAnomaly_Anomaly` FOREIGN KEY (`AnomalyId`) REFERENCES `Anomalies` (`AnomalyId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_RuleAnomaly_Rule` FOREIGN KEY (`RuleId`) REFERENCES `Rules` (`RuleId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `VideoDetectedAnomaly`
--
ALTER TABLE `VideoDetectedAnomaly`
  ADD CONSTRAINT `FK_VideoDetectedAnomaly_DetectedAnomalies` FOREIGN KEY (`DetectedAnomalyId`) REFERENCES `DetectedAnomalies` (`DetectedAnomalyId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_VideoDetectedAnomaly_Videos` FOREIGN KEY (`VideoId`) REFERENCES `Videos` (`VideoId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `VideoDetectedObject`
--
ALTER TABLE `VideoDetectedObject`
  ADD CONSTRAINT `FK_VideoDetectedObjecst_DetectedObjects` FOREIGN KEY (`DetectedObjectId`) REFERENCES `DetectedObjects` (`DetectedObjectId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_VideoDetectedObjecst_Videos` FOREIGN KEY (`VideoId`) REFERENCES `Videos` (`VideoId`);

--
-- Constraints for table `VideoUser`
--
ALTER TABLE `VideoUser`
  ADD CONSTRAINT `FK_VideoUser_Users` FOREIGN KEY (`UserId`) REFERENCES `Users` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_VideoUser_Videos` FOREIGN KEY (`VideoId`) REFERENCES `Videos` (`VideoId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `VideoVideoFeature`
--
ALTER TABLE `VideoVideoFeature`
  ADD CONSTRAINT `FK_VideoVideoFeature_VideoFeatures` FOREIGN KEY (`VideoFeatureId`) REFERENCES `VideoFeatures` (`VideoFeatureId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_VideoVideoFeature_Videos` FOREIGN KEY (`VideoId`) REFERENCES `Videos` (`VideoId`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
