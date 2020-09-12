Beautiful Soup库的基本元素
=============================
1. soup.a:获取a标签的内容  
   
2. soup.a.name:获取a标签的名字
   
3. soup.a.attrs:获取a标签的属性，返回一个字典
   
4. soup.a.string:获取a标签间的字符串/注释（两者类型不同）  

标签树的遍历
=============================
下行遍历
-----------------------------
soup.head.contents:获得head节点的子节点列表   

soup.head.children:用于循环遍历head节点的子节点信息

soup.head.descendants:循环遍历head节点后的所有节点信息（for循环）

上行遍历
-----------------------------
.parent:节点的父亲标签  

.parents:用于循环遍历先辈节点  

html标签的父亲是它自己；soup标签的父亲是空的  

平行遍历
--------------------
.next_sibling:返回按照HTML文本顺序的下一个平行节点标签   

.previous_sibling:返回按照HTML文本顺序的上一个平行节点标签  

.next_siblings:后续所有平行节点标签  
 
.previous_siblings:前续所有平行节点标签  
（平行遍历发生在同一父亲节点下的各节点间）

prettify()
--------------------
能够为HTML文本的标签和内容增加换行符，也可对单个标签做相关处理.

bs4库将读入的HTML文件转化为“UTF-8"编码.

