import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

import java.util.List;
import java.io.FileReader;
import java.io.FileNotFoundException;
import javax.script.ScriptEngineFactory;

public class ScriptEngineExample {
  public static void main(String[] args) {
    ScriptEngineManager manager = new ScriptEngineManager();

    List<ScriptEngineFactory> factories = manager.getEngineFactories();
    // for (ScriptEngineFactory factory : factories) {
    //   System.out.println("Name : " + factory.getEngineName());
    //   System.out.println("Version : " + factory.getEngineVersion());
    //   System.out.println("Language name : " + factory.getLanguageName());
    //   System.out.println("Language version : " + factory.getLanguageVersion());
    //   System.out.println("Extensions : " + factory.getExtensions());
    //   System.out.println("Mime types : " + factory.getMimeTypes());
    //   System.out.println("Names : " + factory.getNames());
    // }

    ScriptEngine engine = manager.getEngineByName("Rhino");
    //System.out.println(engine);
    try {
        engine.eval("print('hihi')");
        engine.eval(new FileReader("js/main.js"));
    } catch (ScriptException e) {
        e.printStackTrace();
    } catch (FileNotFoundException e) {
        e.printStackTrace();
    }
  }
}
