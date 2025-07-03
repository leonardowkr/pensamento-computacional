import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        Funcionario funcionario = new Funcionario("Joao", 40000, "gerente");
        Funcionario funcionario2 = new Funcionario("Gabriel", 80000, "CEO");
        ArrayList<Funcionario> funcionarios = new ArrayList<>();
        funcionarios.add(funcionario);
        funcionarios.add(funcionario2);
        for (Funcionario funcionario1 : funcionarios) {
            System.out.println("Nome do funcionário " + funcionario1.getNome() + ", com salário de " + funcionario1.getSalario()+" no cargo de " + funcionario1.getCargo());
            
        }

    }
}
