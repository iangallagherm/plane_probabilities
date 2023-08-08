prime = 19;

[nil_points, split_points, field_points] = fpPlanePoints(prime);

%figure('Name', 'Nilpotent Points')
%plotPlanePoints(nil_points, 'red');

%figure('Name', 'Split Points')
%plotPlanePoints(split_points, 'green');

%figure('Name', 'Field Points')
%plotPlanePoints(field_points, 'blue');

figure('Name', 'All Points')
view(3);
hold on
plotPlanePoints(nil_points, 'red');
plotPlanePoints(split_points, 'green');
plotPlanePoints(field_points, 'blue');
hold off

function [nil_points, split_points, field_points] = fpPlanePoints(p)
    nil_points = zeros((p - 1) * (p + 1), 3);
    nil_count = 0;
    
    split_points = zeros((p - 1) * ((p * (p + 1)) / 2), 3);
    split_count = 0;
    
    field_points = zeros((p - 1) * ((p * (p - 1)) / 2), 3);
    field_count = 0;
    
    squares = zeros(p, 1);
    for n = 0:p-1
        squares(mod(n^2, p) + 1) = 1;
    end
    
    for x = 0:p - 1
        for y = 0:p - 1
            for z = 0:p - 1
                norm = -x^2 -y^2 + z^2;
                
                if mod(norm, p) == 0
                    nil_count = nil_count + 1;
                    nil_points(nil_count, :) = [x y z];
                elseif squares(mod(-norm, p) + 1) == 1
                    split_count = split_count + 1;
                    split_points(split_count, :) = [x y z];
                else
                    field_count = field_count + 1;
                    field_points(field_count, :) = [x y z];
                end
            end
        end
    end
end

function scatterPlot = plotPlanePoints(points, color)
    scatterPlot = scatter3(points(:, 1), points(:, 2), points(:, 3), 5000, color, '.');
    
    xlabel('i')
    ylabel('j')
    zlabel('k')
    
    ax = gca;
    ax.FontSize = 20;
    
    dx = .05;
    dy = .05;
    dz = .05;
    
    %text(points(:, 1) + dx, points(:, 2) + dy, points(:, 3) + dz, points2str(points))
end

function ptsStr = points2str(points)
    ptsStr = strcat(int2str(points(:, 1)), ',', int2str(points(:, 2)), ',', int2str(points(:, 3)));
end