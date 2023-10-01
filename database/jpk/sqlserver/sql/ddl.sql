/* ---------------------------------------------------- */
/*  Created On : 30-wrz-2023 14:30:52                   */
/*  DBMS       : SQL Server                             */
/* ---------------------------------------------------- */

/* Drop Tables */

IF OBJECT_ID('JPK_NAGLOWEK', 'U') IS NOT NULL
    DROP TABLE JPK_NAGLOWEK;

IF OBJECT_ID('JPK_PODMIOT', 'U') IS NOT NULL
    DROP TABLE JPK_PODMIOT;

IF OBJECT_ID('VAT_SPRZEDAZ', 'U') IS NOT NULL
    DROP TABLE VAT_SPRZEDAZ;

IF OBJECT_ID('VAT_ZAKUP', 'U') IS NOT NULL
    DROP TABLE VAT_ZAKUP;

/* Create Tables with Primary and Foreign Keys, Check, and Unique Constraints */

CREATE TABLE JPK_NAGLOWEK
(
    NAGLOWEK_ID INT NOT NULL PRIMARY KEY,
    CZAS_WYSLANIA DATETIME NOT NULL,
    CZAS_UTWORZENIA DATETIME NOT NULL,
    DATA_OD DATETIME NOT NULL,
    DATA_DO DATETIME NULL,
    ROKMC INT NOT NULL
);

CREATE TABLE JPK_PODMIOT
(
    PODMIOT_ID INT NOT NULL PRIMARY KEY,
    NAGLOWEK_ID INT NOT NULL,
    NIP NVARCHAR(20) NOT NULL,
    IMIE NVARCHAR(255) NOT NULL,
    NAZWISKO NVARCHAR(255) NOT NULL,
    DATA_URODZENIA DATETIME NOT NULL,
    TELEFON INT NULL,
    CONSTRAINT FK_JPK_PODMIOT_JPK_NAGLOWEK FOREIGN KEY (NAGLOWEK_ID) REFERENCES JPK_NAGLOWEK (NAGLOWEK_ID) ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE VAT_SPRZEDAZ
(
    SPRZEDAZ_ID INT NOT NULL PRIMARY KEY,
    NAGLOWEK_ID INT NOT NULL,
    NR_KONTRAHENTA NVARCHAR(255) NOT NULL,
    DOWOD_SPRZEDAZY NVARCHAR(255) NOT NULL,
    DATA_WYSTAWIENIA DATETIME NOT NULL,
    DATA_SPRZEDAZY DATETIME NOT NULL,
    P_6 INT NULL,
    P_8 INT NULL,
    P_9 INT NULL,
    P_11 INT NULL,
    P_13 INT NULL,
    P_15 INT NULL,
    P_16 INT NULL,
    P_19 INT NULL,
    P_96 INT NULL,
    CONSTRAINT FK_VAT_SPRZEDAZ_JPK_NAGLOWEK FOREIGN KEY (NAGLOWEK_ID) REFERENCES JPK_NAGLOWEK (NAGLOWEK_ID) ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE VAT_ZAKUP
(
    ZAKUP_ID INT NOT NULL PRIMARY KEY,
    NAGLOWEK_ID INT NOT NULL,
    NR_DOSTAWCY NVARCHAR(255) NOT NULL,
    DOWOD_ZAKUPU NVARCHAR(255) NOT NULL,
    DATA_ZAKUPU DATETIME NOT NULL,
    DATA_WPLYWU DATETIME NOT NULL,
    P_61 INT NULL,
    P_77 INT NULL,
    P_78 INT NULL,
    CONSTRAINT FK_VAT_ZAKUP_JPK_NAGLOWEK FOREIGN KEY (NAGLOWEK_ID) REFERENCES JPK_NAGLOWEK (NAGLOWEK_ID) ON DELETE NO ACTION ON UPDATE NO ACTION
);