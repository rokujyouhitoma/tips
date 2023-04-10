import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

import java.util.List;
import javax.script.ScriptEngineFactory;

public class Rhino {
  public static void main(String[] args) {
    ScriptEngineManager manager = new ScriptEngineManager();
    //ScriptEngine engine = manager.getEngineByName("");

    List<ScriptEngineFactory> factories = manager.getEngineFactories();
    for (ScriptEngineFactory factory : factories) {
      System.out.println("Name : " + factory.getEngineName());
      System.out.println("Version : " + factory.getEngineVersion());
      System.out.println("Language name : " + factory.getLanguageName());
      System.out.println("Language version : " + factory.getLanguageVersion());
      System.out.println("Extensions : " + factory.getExtensions());
      System.out.println("Mime types : " + factory.getMimeTypes());
      System.out.println("Names : " + factory.getNames());
    }

  }
}
