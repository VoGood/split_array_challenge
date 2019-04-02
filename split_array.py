class split: 
    def __init__(self, input_list : list, splitter : int):
        """ Splits an array into a number of equally-sized sub-arrays.
        
        Parameters
        ----------
        input_list : list
            Input list to be split
        splitter : int
            Number of sub-arrays to be ctreated.
            
        Examples
        --------
        
        >>> from split_array import split
        >>> new_array = split([1,2,3,4,5,6,7],2);
        >>> print(new_array.splitter_operator)
        """
        
        if not isinstance(splitter, int):
            raise TypeError('integer argument expected, got ' + type(splitter).__name__)
        
        if splitter< 1:
            raise ValueError('postive integer argument expected')
            
        self.input_list = input_list;
        self.splitter = splitter;

    @property
    def splitter_operator(self) -> list:
        """
        :return: The total price of the trade
        """
        return [self.input_list[n:n+self.splitter] for n in range(0, len(self.input_list), self.splitter)]
