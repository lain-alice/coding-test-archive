function solution(sides) {
    
    // if (Math.max(...sides) < Math.min(...sides) +  ) return 1;
    
    sides.sort((a, b) => a - b);
    
    return (sides[0] + sides[1] > sides[2] ? 1 : 2)
        
    return 2;
    
    
}