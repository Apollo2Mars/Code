
  
-------------------------------------------------------------------------
# 基本语法:
	(parameters) -> expression
	或
	(parameters) ->{ statements; }

# Reference Website
+ http://blog.csdn.net/renfufei/article/details/24600507

# Example
```
	String[] atp = {"Rafael Nadal", "Novak Djokovic",  
	       "Stanislas Wawrinka",  
	       "David Ferrer","Roger Federer",  
	       "Andy Murray","Tomas Berdych",  
	       "Juan Martin Del Potro"};  
	List<String> players =  Arrays.asList(atp);  

	// 以前的循环方式  
	for (String player : players) {  
	     System.out.print(player + "; ");  
	}  

	// 使用 lambda 表达式以及函数操作(functional operation)  
	players.forEach((player) -> System.out.print(player + "; "));  

	// 在 Java 8 中使用双冒号操作符(double colon operator)  
	players.forEach(System.out::println);  
```

# Craft
```
    public List<Word> changeWordList2CharList(List<Word> list_word){
        StringBuffer sb = new StringBuffer();
        list_word.forEach((word)-> sb.append(word.getRawText()));
        String sLine = sb.toString();

        ArrayList<Word> list_char = new ArrayList<>();

        return  list_char;
    }
```
-----------------------------------------------------------------------------
 long start = System.currentTimeMillis();
 /**
 *  do some works
 */
 long end = System.currentTimeMillis();
 long time  = end - start;
 System.out.println("Loading model spent " + time + " ms");
 
--------------------------------------------------
    File inputFile = new File("/home/train.json");
    InputStream inputStream = new FileInputStream(inputFile);

    /** Read **/
    BufferedReader reader = null;
    try{
      reader = new BufferedReader(new FileReader(inputFile));
      String string = null;
      while ((string = reader.readLine()) != null){
        System.out.println(string);
      }
    }catch (Exception e){
      e.printStackTrace();
    }
    System.out.println(inputStream.read());