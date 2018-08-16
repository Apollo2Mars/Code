+ 快速排序
```
public static void sort(int array[], int low, int high){
	int i,j;
	int key;
	if(low >= high){
		return;
	}
	i = low;
	j = high;
	//
	key = arrar[i];
	while(i<j){
		while(i<j && array[j] >= key){
			j--;
		}
        if(i < j){
			array[i++] = array[j];
	    }
	    while(i<j && array[i] < key){
			i++;
	    }
	    if(i<j){
			array[j--] == array[i];
	    }
	}
	array[i] = key;
	sort(array, low, i-1);
	sort(array, i+1, high);
}
```
