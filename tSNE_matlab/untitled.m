testVecs = importdata('testVecs.mat');

testVecs = testVecs([5001:size(testVecs,1)],:);

%%
size(testVecs)
%size(words) 
dims = tsne(testVecs, [], 2, size(testVecs,2));
%%
dlmwrite('vectors.txt',dims,'delimiter',' ','-append');
%%
dims = importdata('vectors.txt')
%% 3D
clf
plot3(dims(:,1),dims(:,2), dims(:,3),'.')
hold on
for i = 1: length(dims(:,1))
text(dims(i,1),dims(i,2),dims(i,3),wordsStruct(i,:))
end

%% 2D
clf
plot(dims(:,1),dims(:,2),'*g','MarkerSize',1)
hold on
for i = 1: length(dims(:,1))
    if(strcmp(cellstr(wordsStruct(i,:)),char('malware')))
        mal = i;
    end
    %text(dims(i,1),dims(i,2),wordsStruct(i,:))
end

plot(dims(mal,1),dims(mal,2),'b*')
text(dims(mal,1),dims(mal,2),wordsStruct(mal,:),'Color','Blue','FontSize',14)
