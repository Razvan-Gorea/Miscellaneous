public class LogLevels {
    
    public static String message(String logLine) {
        logLine = logLine.substring(logLine.lastIndexOf(": ") + 1).trim();
        return logLine.trim();
    }

    public static String logLevel(String logLine) {
        logLine = logLine.substring(logLine.indexOf("[") + 1).trim();
        logLine = logLine.substring(0, logLine.indexOf("]")).trim();
        logLine = logLine.toLowerCase().trim();
        return logLine.trim();
    }

    public static String reformat(String logLine) {
        String logLineMessage = logLine.substring(logLine.lastIndexOf(": ") + 1).trim();
        String logLineLevel = logLine.substring(logLine.indexOf("[") + 1).trim();
        logLineLevel = logLineLevel.substring(0, logLineLevel.indexOf("]")).trim();
        logLineLevel = logLineLevel.toLowerCase().trim();
        String completedMessage = logLineMessage + " (" + logLineLevel + ")".trim();
        return completedMessage.trim();
    }
}