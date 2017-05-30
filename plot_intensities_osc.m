figure5=figure;

%% Create random sample from Trigger Index with a sample size of 100 (No replacement)
k=randsample(length(RESULTS.files{1, 1}.TriggerIndex),100,false);

% To view the intensity plots of a random sample comment 'for r =1:length(RAWDATA.files{1, 1});' below
% and uncomment 'for i = 1:k(end); r = k(i);' right below.
index = 1;
decisionlist = ones (k(end),1);
        for i = 1:k(end)
        r = k(i);
        
%% To view the intensity plots of all of the cells comment 'for i = 1:k(end); 
%  r = k(i);' right above, and uncomment 'for r =1:length(RAWDATA.files{1, 1});' right below    


%for r =1:length(RAWDATA.files{1, 1});
   
     %trigger and oscillating
     if RESULTS.files{1,1}.SinglePeakIndex(r) == 1 && RESULTS.files{1,1}.TriggerIndex(r) == 1
         subplot(3,1,1)
         plot(RAWDATA.files{1,1}(r).intensity(:))
         title('Oscillatory Peak')
         ylim([0 1.5])
         set(gca,'YGrid','on','YMinorGrid','on');
         
       % pause
          % hold on
         %data_oscillating(:,r) = RAWDATA.files{1,1}(r).intensity(:);
         
         

     %trigger and single
     elseif RESULTS.files{1,1}.SinglePeakIndex(r) == 0 && RESULTS.files{1,1}.TriggerIndex(r) == 1
         subplot(3,1,2)
         plot(RAWDATA.files{1,1}(r).intensity(:))
         title('Single Peak')
         ylim([0 1.5])
         set(gca,'YGrid','on','YMinorGrid','on');
        % pause
         % hold on
         %data_single(:,r) = RAWDATA.files{1,1}(r).intensity(:);
         
%         pause

     elseif RESULTS.files{1,1}.TriggerIndex(r) == 0 
         subplot(3,1,3)
         plot(RAWDATA.files{1,1}(r).intensity(:))
         title('Non-Trigger')
         ylim([0 1.5])
         set(gca,'YGrid','on','YMinorGrid','on');
         %pause
         
        %   hold on
        % data_single(:,r) = RAWDATA.files{1,1}(r).intensity(:);
        % pause
     end
 pause%(.5)
%hold on


%%Determine whether a cell is a True Postive(0), False Positive(1), False Negative(2), or True Negative(3) for trig/non-trig
% prompt = 'Is the cell a True Postive(0), False Positive(1), False Negative(2), or True Negative(3) for trig/non-trig?';
% ans = input(prompt);
% if ans==0
%     true_positive=1;
%     
% elseif ans==1
%     false_postive=1;
%     
% elseif ans==2
%     false_negative=1;
%     
% elseif ans==3
%     true_negative=1;
% end
        
        prompt = 'Is the cell a True Postive(0), False Positive(1), False Negative(2), or True Negative(3) for trig/non-trig?';
        decision = input(prompt);
        
        decisionlist(index,1) = decision;
        index = index + 1;

%%Calculate number of Accuracy of CalQuo2 
    true_positive=sum(decisionlist(:)==0);
    false_positive=sum(decisionlist(:)==1);
    false_negative=sum(decisionlist(:)==2);
    true_negative=sum(decisionlist(:)==3);
        end
%decisionlist(r,1) =decision;

%%Calculate number of Accuracy of CalQuo2 
%     true_positive=sum(decisionlist(:)==0);
%     false_positive=sum(decisionlist(:)==1);
%     false_negative=sum(decisionlist(:)==2);
%     true_negative=sum(decisionlist(:)==3);

