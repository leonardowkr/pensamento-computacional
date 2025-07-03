public abstract class Semaforo {
    protected String cor;
    protected String nome;

    public Semaforo(String cor, String nome){
        this.cor = cor;
        this.nome = nome;
    }
    public abstract void mudarCor();

    public String getCor(){
        return this.cor;
    }
    
    public String getNome(){
        return this.nome;
    }
    //Méotdo abstrato
    
    public void esperar(int segundos){
        try{
            Thread.sleep(segundos * 1000);
        }
        catch (InterruptedException e){
            e.printStackTrace();
        }
    }
    public void status(){
        String textColor = "\u001B[31m";
        if(this.cor == "verde"){
            textColor = "\u001B[32m";
        }
        else if(this.cor == "amarelo"){
            textColor = "\u001B[33m";
        }
        textColor += this.cor + "\u001B[0m";
        System.out.println("Semaforo " + this.nome + " está: " + textColor);
    }

}
