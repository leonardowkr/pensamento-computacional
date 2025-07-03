public class SemaforoVeicular extends Semaforo {
    public SemaforoVeicular(String cor, String nome){
            super(cor, nome);
            
        }

    @Override
    public void mudarCor() {
        switch (this.cor) {
            case "vermelho":
                this.cor = "verde";
                break;
            case "verde":
                this.cor = "amarelo";
                break;

            case "amarelo":
                this.cor = "vermelho";
                break;
        }
        status();
    }
}
