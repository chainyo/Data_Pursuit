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
(401, 'Quelle est la forme d\'une fonction affine', 5, 1),
(402, 'La courbe en cloche est une caractéristique de la loi', 5, 2),
(403, 'Qui est le créateur de l\'algorithme du \'Shortest path\' en 1959', 5, 3),
(404, 'Quelle est la médiane de cette liste [1, 1, 3, 4, 7, 9, 12, 12, 15]', 5, 1),
(405, 'Quel est le moyenne de cette liste [13, 5, 7, 0, 25]', 5, 1),
(406, 'La variance peut être négative', 5, 1),
(407, 'Quel concept appartient à l\'algèbre de Boole', 5, 2),
(408, 'Quel est le rapport de l\'écart-type à la variance', 5, 2),
(409, 'Parmi ces choix, lequel est un vecteur', 5, 1),
(410, 'Qu\'est-ce qu\'une matrice', 5, 1),
(411, 'Le Coefficient de détermination est le carré du coefficient de', 5, 2),
(412, 'Avec combien de matrice(s) peut-on représenter une image RGB', 5, 1),
(413, 'A quoi correspond le 3ème quantile', 5, 1),
(414, 'Combien de colonne comportera une matrice comportant 10 variables', 5, 1),
(415, 'Le nombre de colonnes de la 1ère matrice doit-il correspondre au nombre de lignes de la 2ème matrice ?', 5, 2),
(416, 'Le calcul matriciel de structure (2,3)*(2,3) est-il possible', 5, 2),
(417, 'En tirant une carte au hasard dans un jeu de 32 cartes, la probabilité d\'obtenir une Reine rouge est', 5, 1),
(418, 'Quel test de corrélation doit-on utiliser quand nos variables suivent une loi normale', 5, 2),
(419, 'Il n\'y a aucune corrélation entre 2 variables lorsque le rapport est de -1', 5, 2),
(420, 'Quelle est la célèbre épreuve utiliser dans la loi binomiale de notation n', 5, 3),
(421, 'Une courbe polynomiale indique que plusieurs variables existent dans notre dataset', 5, 2),
(422, 'Pour f(x) = 2x² + 4x + 5, la courbe passerait l\'origine à quelle ordonée ?',5, 2),
(423, 'Le coefficient directeur peut-il indiquer l\'évolution d\'une droite ',5,1),
(424,'En statistique, un outlier est une valeur ',5,1),
(425,'La valeur sigma d\'une Loi Normale correspond à ',5,1),
(426,'Laquelle de ces propositions présente une forte relation entre x et y ',5,3),
(427,'L\'erreur quadratique moyenne est la racine de ',5,3),
(428,'La somme des carrés des résidus n\'est pas un indicateur de comparaison de 2 séries de valeurs',5,3),
(429,'La variance est une mesure du degré de dispersion d\'un ensemble de données',5,2),
(430,'L\'équation (ih/2 π) d l Ψ>/dt = Hl Ψ> peut-elle être résolue par Paul ?',5,1);

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
(401, 401, 'Sinusoïdale', 0),
(402, 401, 'Exponentielle', 0),
(403, 401, 'Droite', 1),
(404, 402, 'de Gauss', 1),
(405, 402, 'Fisher', 0),
(406, 402, 'de Shapiro-Wilk', 0),
(407, 403, 'Dijkstra', 1),
(408, 404, '7', 1),
(409, 405, '10', 1),
(410, 406, 'Vrai', 0),
(411, 406, 'Faux', 1),
(412, 407, 'XOR', 1),
(413, 407, 'OR', 0),
(414, 407, 'AND', 0),
(415, 408, 'le carré', 0),
(416, 408, 'le cube', 0),
(417, 408, 'la racine', 1),
(418, 409, '3', 0),
(419, 409, '[3 0 1]', 1),
(420, 409, '3-0-1', 0),
(421, 410, 'un tableau', 1),
(422, 410, 'un graphique', 0),
(423, 410, 'un test', 0),
(424, 411, 'variation', 0),
(425, 411, 'linéaire', 0),
(426, 411, 'corrélation', 1),
(427, 412, '3', 1),
(428, 413, '75%', 1),
(429, 414, '10', 1),
(430, 415, 'Vrai', 1),
(431, 415, 'Faux', 0),
(432, 416, 'Vrai', 0),
(433, 416, 'Faux', 1),
(434, 417, '4/32', 0),
(435, 417, '2/16', 0),
(436, 417, '1/16', 1),
(437, 418, 'Kendall', 0),
(438, 418, 'Pearson', 1),
(439, 418, 'Spearman', 0),
(440, 419, 'Vrai', 0),
(441, 419, 'Faux', 1),
(442, 420,'Bernoulli', 1),
(443, 421,'Vrai',0),
(444, 421,'Faux',1),
(445, 422,'5',1),
(446, 423,'Vrai',1),
(447, 423,'Faux',0),
(448, 424,'Abérrante',1),
(449, 424,'Absente',0),
(450, 424,'Fréquente',0),
(451, 425,'La variance',0),
(452, 425,'L\'écart-type',1),
(453, 425,'La moyenne',0),
(454, 426,'Corrélation = 0.9',1),
(455, 426,'P-value = 1',0),
(456, 426,'La réponse D',0),
(457,427,'la MSE',1),
(458,427,'la EAM',0),
(459,427,'la THOMAS',0),
(460,428,'Vrai',0),
(461,428,'Faux',1),
(462,429,'Vrai',1),
(463,429,'Faux',0),
(464,430,'Vrai',1),
(465,430,'Faux',0);

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
(1, 'Big Data'),
(2, 'IA'),
(3, 'Ethique'),
(4, 'Python'),
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
