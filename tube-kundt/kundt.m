clear all;
close all;

% Tube de Kundt: tracé des graphes d'absorption

%% === Mesures de coefficient ===

% Vecteur fréquence
f = [63, 125, 250, 500, 1000, 2000];

%% Tube de Kundt fermé
tube63 = 0;
tube125 = 0;
tube250 = 0;
tube500 = 0;
tube1000 = 0;
tube2000 = 0;

abs_tube = [tube63, tube125 ,tube250, tube500, tube1000, tube2000];

%% Polystyrène
poly63 = 0;
poly125 = 0;
poly250 = 0;
poly500 = 0;
poly1000 = 0;
poly2000 = 0;

abs_poly = [poly63, poly125 ,poly250, poly500, poly1000, poly2000];

%% Mousse Souple
mousse63 = 0;
mousse125 = 0;
mousse250 = 0;
mousse500 = 0;
mousse1000 = 0;
mousse2000 = 0;

abs_mousse = [mousse63, mousse125 ,mousse250, mousse500, mousse1000, mousse2000];

%% Laine de roche
laine63 = 0;
laine125 = 0;
laine250 = 0.75;
laine500 = 0;
laine1000 = 0;
laine2000 = 0;

abs_laine = [laine63, laine125 ,laine250, laine500, laine1000, laine2000];

%% Tracé du graph

figure;
plot(f, abs_tube, f, abs_poly, f, abs_mousse, f, abs_laine, '.-');
legend('Tube','Polystyrène','Mousse Souple','Laine de roche');
xlabel('fréquence (Hz)');
ylabel('coefficient d''absorption');
axis([50,2200,0,1.1])
title('Coefficient d''absorption de différents matériaux en fonction de la fréquence');
saveas(gcf, 'coef_abs', 'png')
