public class App {
    public static void main(String[] args) throws Exception {
        SemaforoVeicular semaforoA = new SemaforoVeicular("vermelho", "A");
        SemaforoVeicular semaforoB = new SemaforoVeicular("vermelho", "B");
        while (true){
            semaforoB.status();
            semaforoA.mudarCor();           // verde
            semaforoA.esperar(5);
            
            System.out.println();
            semaforoB.status();
            semaforoA.mudarCor();          // amarelo
            semaforoA.esperar(1);   
            
            System.out.println();
            semaforoB.status();
            semaforoA.mudarCor();           // vermelho
            semaforoB.esperar(1);

            System.out.println();
            semaforoB.mudarCor();           // verde
            
            semaforoA.status();
            semaforoB.esperar(5);
            
            System.out.println();
            semaforoB.mudarCor();           // amarelo
            semaforoA.status();
            semaforoB.esperar(1);

            System.out.println();
            semaforoB.mudarCor();           // vermelho
            semaforoA.status();
            semaforoA.esperar(1);
            System.out.println();
        }
}
}
