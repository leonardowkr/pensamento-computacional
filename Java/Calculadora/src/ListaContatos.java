import java.util.ArrayList;
import java.util.HashMap;

public class ListaContatos {
    public static void main(String[] args) {
        ArrayList<HashMap<String, String>> contatos = new ArrayList<>();
        // Criando um contato
        HashMap<String, String> contato1 = new HashMap<>();
        contato1.put("nome", "João");
        contato1.put("telefone", "123456789");
        contatos.add(contato1);
        HashMap<String, String> contato2 = new HashMap<>();
        contato2.put("nome", "Maria");
        contato2.put("telefone", "987654321");
        contatos.add(contato2);
        // Listando contatos
        for (HashMap<String, String> contato : contatos) {
            System.out.println("Nome: " + contato.get("nome") +
                    ", Telefone: " + contato.get("telefone"));
        }
    }
}