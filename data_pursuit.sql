-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:8081
-- Généré le : jeu. 26 nov. 2020 à 17:17
-- Version du serveur :  5.7.24
-- Version de PHP : 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `data_poursuit`
--
CREATE DATABASE IF NOT EXISTS `data_pursuit` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `data_pursuit`;

-- --------------------------------------------------------

--
-- Structure de la table `joueurs`
--

CREATE TABLE `joueurs` (
  `id_joueur` int(11) NOT NULL,
  `nom_joueur` varchar(50) NOT NULL,
  `points_joueur` int(11) NOT NULL,
  `couleur_joueur` char(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `questions`
--

CREATE TABLE `questions` (
  `id_question` int(7) NOT NULL,
  `libelle_question` text NOT NULL,
  `id_theme` int(1) NOT NULL,
  `difficulte_question` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `questions`
--

INSERT INTO `questions` (`id_question`, `libelle_question`, `id_theme`, `difficulte_question`) VALUES
(1, 'Quelle est la forme d\'une fonction affine', 5, 1),
(2, 'La courbe en cloche est une caractéristique de la loi', 5, 2),
(3, 'Qui est le créateur de l\'algorithme du \'Shortest path\' en 1959', 5, 3),
(4, 'Quelle est la médiane de cette liste [1, 1, 3, 4, 7, 9, 12, 12, 15]', 5, 1),
(5, 'Quel est le moyenne de cette liste [13, 5, 7, 0, 25]', 5, 1),
(6, 'La variance peut être négative', 5, 1),
(7, 'Quel concept appartient à l\'algèbre de Boole', 5, 2),
(8, 'Quel est le rapport de l\'écart-type à la variance', 5, 2),
(9, 'Parmi ces choix, lequel est un vecteur', 5, 1),
(10, 'Qu\'est-ce qu\'une matrice', 5, 1),
(11, 'Le Coefficient de détermination est le carré du coefficient de', 5, 2),
(12, 'Avec combien de matrice(s) peut-on représenter une image RGB', 5, 1),
(13, 'A quoi correspond le 3ème quantile', 5, 1),
(14, 'Combien de colonne comportera une matrice comportant 10 variables', 5, 1),
(15, 'Le nombre de colonnes de la 1ère matrice doit-il correspondre au nombre de lignes de la 2ème matrice ?', 5, 3),
(16, 'Le calcul matriciel de structure (2,3)*(2,3) est-il possible', 5, 2),
(17, 'En tirant une carte au hasard dans un jeu de 32 cartes, la probabilité d\'obtenir une Reine rouge est', 5, 1),
(18, 'Quel test de corrélation doit-on utiliser quand nos variables suivent une loi normale', 5, 2),
(19, 'Il n\'y a aucune corrélation entre 2 variables lorsque le rapport est de -1', 5, 2);

-- --------------------------------------------------------

--
-- Structure de la table `reponses`
--

CREATE TABLE `reponses` (
  `id_reponse` int(7) NOT NULL,
  `id_question` int(7) NOT NULL,
  `libelle_reponse` varchar(100) NOT NULL,
  `valeur_reponse` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `reponses`
--

INSERT INTO `reponses` (`id_reponse`, `id_question`, `libelle_reponse`, `valeur_reponse`) VALUES
(1, 1, 'Sinusoïdale', 0),
(2, 1, 'Exponentielle', 0),
(3, 1, 'Droite', 1),
(4, 2, 'de Gauss', 1),
(5, 2, 'Fisher', 0),
(6, 2, 'de Shapiro-Wilk', 0),
(7, 3, 'Dijkstra', 1),
(8, 4, '7', 1),
(9, 5, '10', 1),
(10, 6, 'Vrai', 0),
(11, 6, 'Faux', 1),
(12, 7, 'XOR', 1),
(13, 7, 'OR', 0),
(14, 7, 'AND', 0),
(15, 8, 'le carré', 0),
(16, 8, 'le cube', 0),
(17, 8, 'la racine', 1),
(18, 9, '3', 0),
(19, 9, '[3 0 1]', 1),
(20, 9, '3-0-1', 0),
(21, 10, 'un tableau', 1),
(22, 10, 'un graphique', 0),
(23, 10, 'un test', 0),
(24, 11, 'variation', 0),
(25, 11, 'linéaire', 0),
(26, 11, 'corrélation', 1),
(27, 12, '3', 1),
(28, 13, '75%', 1),
(29, 14, '10', 1),
(30, 15, 'Vrai', 1),
(31, 15, 'Faux', 0),
(32, 16, 'Vrai', 0),
(33, 16, 'Faux', 1),
(34, 17, '4/32', 0),
(35, 17, '2/16', 0),
(36, 17, '1/16', 1),
(37, 18, 'Kendall', 0),
(38, 18, 'Pearson', 1),
(39, 18, 'Spearman', 0),
(40, 19, 'Vrai', 0),
(41, 19, 'Faux', 1);

-- --------------------------------------------------------

--
-- Structure de la table `theme`
--

CREATE TABLE `theme` (
  `id_theme` int(1) NOT NULL,
  `nom_theme` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `theme`
--

INSERT INTO `theme` (`id_theme`, `nom_theme`) VALUES
(1, 'data1'),
(2, 'data2'),
(3, 'data3'),
(4, 'data4'),
(5, 'Mathematiques');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `joueurs`
--
ALTER TABLE `joueurs`
  ADD PRIMARY KEY (`id_joueur`);

--
-- Index pour la table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id_question`),
  ADD KEY `id_theme` (`id_theme`);

--
-- Index pour la table `reponses`
--
ALTER TABLE `reponses`
  ADD PRIMARY KEY (`id_reponse`),
  ADD KEY `id_question` (`id_question`);

--
-- Index pour la table `theme`
--
ALTER TABLE `theme`
  ADD PRIMARY KEY (`id_theme`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `joueurs`
--
ALTER TABLE `joueurs`
  MODIFY `id_joueur` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `questions`
--
ALTER TABLE `questions`
  MODIFY `id_question` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `reponses`
--
ALTER TABLE `reponses`
  MODIFY `id_reponse` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT pour la table `theme`
--
ALTER TABLE `theme`
  MODIFY `id_theme` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `questions`
--
ALTER TABLE `questions`
  ADD CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`id_theme`) REFERENCES `theme` (`id_theme`);

--
-- Contraintes pour la table `reponses`
--
ALTER TABLE `reponses`
  ADD CONSTRAINT `reponses_ibfk_1` FOREIGN KEY (`id_question`) REFERENCES `questions` (`id_question`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
