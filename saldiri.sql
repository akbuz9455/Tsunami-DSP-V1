-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 16 May 2016, 04:24:11
-- Sunucu sürümü: 5.6.17
-- PHP Sürümü: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Veritabanı: `vt`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `saldiri`
--

CREATE TABLE IF NOT EXISTS `saldiri` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `saldiri_ip` text NOT NULL,
  `saldiri_sure` int(11) NOT NULL,
  `saldiri_port` text NOT NULL,
  `saldiri_kontrol` text NOT NULL,
  `uykukontrol` int(11) NOT NULL,
  `askergucu` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Tablo döküm verisi `saldiri`
--

INSERT INTO `saldiri` (`id`, `saldiri_ip`, `saldiri_sure`, `saldiri_port`, `saldiri_kontrol`, `uykukontrol`, `askergucu`) VALUES
(2, '176.40.150.206', 10, '80', '1', 20, 3);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
