package si.f5.mitminecraft.sushida;

import java.io.IOException;

import org.bukkit.plugin.java.JavaPlugin;


public class Main extends JavaPlugin {
    public static Main plugin;

    public Main() throws IOException {
        plugin = this;
    }

    @Override
    public void onEnable(){
        getServer().getScheduler().scheduleSyncRepeatingTask(this, new Runnable(){
            @Override
            public void run() {
                Sushida.removeCd();
            }
        }, 0L, 20L);
		getCommand("typing").setExecutor(new Sushida());
        getCommand("entyping").setExecutor(new Engda());
        getCommand("sushida").setExecutor(new Start());
        getLogger().info("----------------------");
        getLogger().info("This is Sushida!!");
        getLogger().info("Succesfully loaded!!");
        getLogger().info("----------------------");
    }
}
