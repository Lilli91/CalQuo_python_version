%% Randomly plot the normalized internsity profiles of 10% of the population, 
%separated by those that trigger vs. those that don't trigger.  
clear handel;
figure4=figure;
set(figure4, 'Position', [100 100 1500 500])

%% Set time from frames to seconds based on frame rate
x=(0:0.82:819.18); 
%x=[0:0.82:737.18];

%% Create random sample from Trigger Index with a sample size of 100 (No replacement)
%k=randsample(length(RESULTS.files{1, 1}.TriggerIndex),100,false);

%% Create random sample from Trigger Index with a sample size that is 10% of  population size (No replacement)
%k=randsample(length(RESULTS.files{1, 1}.TriggerIndex),round(0.1*(length(RESULTS.files{1, 1}.TriggerIndex))),false);
%k=randsample(length(RESULTS.files{1, 1}.TriggerIndex),round(0.1*(length(RESULTS.files{1, 1}.TriggerIndex))),false);

% for r=1:size(RESULTS.files{1, 1}.TriggerIndex);

%% To view the intensity plots of a random sample comment 'for r =1:length(RAWDATA.files{1, 1});' below
% and uncomment 'for i = 1:k(end); r = k(i);' right below. 
        for i = 1:length(k)
        r = k(i);

%% To view the intensity plots of all of the cells comment 'for i = 1:k(end); 
%  r = k(i);' right above, and uncomment 'for r =1:length(RAWDATA.files{1, 1});' right below    


%for r =1:length(RAWDATA.files{1, 1});
    if RESULTS.files{1, 1}.TriggerIndex  (r)==1
        subplot(1,2,1); 
        %pp=plot(x,RAWDATA.files{1, 1}(r).intensity);
        pp=plot(RAWDATA.files{1, 1}(r).intensity);
        ylim([0 1.2])
        %xlim([0 900])
        ylabel1=ylabel('Normalized Intensity (a.u)','FontName','Arial','FontWeight','bold','FontSize',10);
        set(ylabel1,'Position',[-150,0.5]);
        xlabel1=xlabel('Time(s)','FontName','Arial','FontWeight','bold','FontSize',10);
        set(xlabel1,'Position',[450,-0.15]);
        %handel=title('Trigger Response Function','FontName','Arial','FontSize',20);
%        set(handel,'Position',[450,1.1]);
        set(gca,'YGrid','on','YMinorGrid','off','MinorGridLineStyle','-','FontWeight','Bold','FontName','Arial','FontSize',15);
        
%         'YGrid' 'on'
%         pp.XGrid= 'on';
%         axis square
%         subplot(1,3,3)
%         imagesc(RAWDATA.files{1, 1}(r).phi_b_all)
         axis square
%         
%         sv(RAWDATA.files{1, 1}(r).subregion)
    elseif RESULTS.files{1, 1}.TriggerIndex  (r)==0
        subplot(1,2,2); 
        %pp=plot(x,RAWDATA.files{1, 1}(r).intensity);
        pp=plot(RAWDATA.files{1, 1}(r).intensity);
        ylim([0 1.2])
        %xlim([0 900])
        ylabel2=ylabel('Normalized Intensity (a.u.)','FontName','Arial','FontWeight','bold','FontSize',10);
        set(ylabel2,'Position',[-150,0.5]);
        xlabel2=xlabel('Time(s)','FontName','Arial','FontWeight','bold','FontSize',10);
        set(xlabel2,'Position',[450,-0.15]);
       % handel2=title('Non-Triggered Response Function','FontName','Arial','FontSize',20);
       % set(handel2,'Position',[450,1.1]);
        set(gca,'YGrid','on','YMinorGrid','off','MinorGridLineStyle','-','FontWeight','Bold','FontName','Arial','FontSize',15);
        
        %grid on
%         'YGrid' 'on'
        axis square
%         subplot(1,3,3)
%         imagesc(RAWDATA.files{1, 1}(r).phi_b_all)
%          axis square
%         
%         sv(RAWDATA.files{1, 1}(r).subregion)
    end
    pause;
    %hold on;
end
%
%sv(finalImage.files{1, 1})