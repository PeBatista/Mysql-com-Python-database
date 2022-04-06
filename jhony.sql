-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 16-Fev-2022 às 00:11
-- Versão do servidor: 10.4.20-MariaDB
-- versão do PHP: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `jhony`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `carros`
--

CREATE TABLE `carros` (
  `id_fabrica` int(3) DEFAULT NULL,
  `nomecarro` varchar(45) DEFAULT NULL,
  `id_carro` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `carros`
--

INSERT INTO `carros` (`id_fabrica`, `nomecarro`, `id_carro`) VALUES
(2, 'Civic', 2);

-- --------------------------------------------------------

--
-- Estrutura da tabela `clientes`
--

CREATE TABLE `clientes` (
  `id_carros` int(3) DEFAULT NULL,
  `nomedele` varchar(45) DEFAULT NULL,
  `id_clientes` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `clientes`
--

INSERT INTO `clientes` (`id_carros`, `nomedele`, `id_clientes`) VALUES
(2, 'Pedro', 2);

-- --------------------------------------------------------

--
-- Estrutura da tabela `criadorf`
--

CREATE TABLE `criadorf` (
  `nomedele` varchar(45) DEFAULT NULL,
  `idade` int(3) DEFAULT NULL,
  `id_criador` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `criadorf`
--

INSERT INTO `criadorf` (`nomedele`, `idade`, `id_criador`) VALUES
('Takahiro Hachigo', 62, 2);

-- --------------------------------------------------------

--
-- Estrutura da tabela `fabrica`
--

CREATE TABLE `fabrica` (
  `id_fabrica` int(3) NOT NULL,
  `nomefabrica` varchar(45) DEFAULT NULL,
  `id_criador` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `fabrica`
--

INSERT INTO `fabrica` (`id_fabrica`, `nomefabrica`, `id_criador`) VALUES
(2, 'Honda', 2);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `carros`
--
ALTER TABLE `carros`
  ADD PRIMARY KEY (`id_carro`),
  ADD KEY `id_fabrica` (`id_fabrica`);

--
-- Índices para tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_clientes`),
  ADD KEY `id_carros` (`id_carros`);

--
-- Índices para tabela `criadorf`
--
ALTER TABLE `criadorf`
  ADD PRIMARY KEY (`id_criador`);

--
-- Índices para tabela `fabrica`
--
ALTER TABLE `fabrica`
  ADD PRIMARY KEY (`id_fabrica`),
  ADD KEY `id_criador` (`id_criador`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `carros`
--
ALTER TABLE `carros`
  ADD CONSTRAINT `carros_ibfk_1` FOREIGN KEY (`id_fabrica`) REFERENCES `fabrica` (`id_fabrica`);

--
-- Limitadores para a tabela `clientes`
--
ALTER TABLE `clientes`
  ADD CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`id_carros`) REFERENCES `carros` (`id_carro`);

--
-- Limitadores para a tabela `fabrica`
--
ALTER TABLE `fabrica`
  ADD CONSTRAINT `fabrica_ibfk_1` FOREIGN KEY (`id_criador`) REFERENCES `criadorf` (`id_criador`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
