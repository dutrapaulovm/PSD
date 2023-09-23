-- -----------------------------------------------------
-- Schema teatro
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `teatro` DEFAULT CHARACTER SET utf8mb4 ;
USE `teatro` ;

-- -----------------------------------------------------
-- Table `teatro`.`peca`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `teatro`.`peca` (
  `CODPECA` INT(11) NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(300) NULL DEFAULT NULL,
  PRIMARY KEY (`CODPECA`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `teatro`.`teatro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `teatro`.`teatro` (
  `CODTEATRO` INT(11) NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(300) NOT NULL DEFAULT '',
  `CAPACIDADEASSENTOS` INT NOT NULL,
  PRIMARY KEY (`CODTEATRO`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `teatro`.`apresentacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `teatro`.`apresentacao` (
  `CODAPRESENTACAO` INT(11) NOT NULL AUTO_INCREMENT,
  `CODTEATRO` INT(11) NOT NULL,
  `CODPECA` INT(11) NOT NULL,
  `QUANTIDADEPUBLICO` INT(11) NOT NULL DEFAULT 0,
  `DATA` DATE NOT NULL DEFAULT '0000-00-00',
  PRIMARY KEY (`CODAPRESENTACAO`),
  INDEX `FK_TEATRO_AP` (`CODTEATRO` ) ,
  INDEX `FK_PECA_AP` (`CODPECA` ) ,
  CONSTRAINT `FK_PECA_AP`
    FOREIGN KEY (`CODPECA`)
    REFERENCES `teatro`.`peca` (`CODPECA`),
  CONSTRAINT `FK_TEATRO_AP`
    FOREIGN KEY (`CODTEATRO`)
    REFERENCES `teatro`.`teatro` (`CODTEATRO`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `teatro`.`ator`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `teatro`.`ator` (
  `CODATOR` INT(11) NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(300) NULL DEFAULT NULL,
  PRIMARY KEY (`CODATOR`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `teatro`.`atorpeca`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `teatro`.`atorpeca` (
  `CODPECA` INT(11) NOT NULL,
  `CODATOR` INT(11) NOT NULL,
  PRIMARY KEY (`CODPECA`, `CODATOR`),
  INDEX `FK_ATOR_ATORPECA` (`CODATOR` ) ,
  CONSTRAINT `FK_ATOR_ATORPECA`
    FOREIGN KEY (`CODATOR`)
    REFERENCES `teatro`.`ator` (`CODATOR`),
  CONSTRAINT `FK_PECA_ATORPECA`
    FOREIGN KEY (`CODPECA`)
    REFERENCES `teatro`.`peca` (`CODPECA`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `teatro`.`ingresso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `teatro`.`ingresso` (
  `CODINGRESSO` INT(11) NOT NULL AUTO_INCREMENT,
  `CODAPRESENTACAO` INT(11) NOT NULL,
  `TIPOCADEIRA` VARCHAR(1) NOT NULL DEFAULT 'S',
  `DATA` DATE NOT NULL DEFAULT '0000-00-00',
  `PRECO` DOUBLE NOT NULL DEFAULT 0,
  PRIMARY KEY (`CODINGRESSO`),
  INDEX `FK_AP_INGRESSO` (`CODAPRESENTACAO` ) ,
  CONSTRAINT `FK_AP_INGRESSO`
    FOREIGN KEY (`CODAPRESENTACAO`)
    REFERENCES `teatro`.`apresentacao` (`CODAPRESENTACAO`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;