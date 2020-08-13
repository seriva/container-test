package com.helloworld.helloworld.models;

import java.io.Serializable;

public class HelloModel implements Serializable {
    String message;
    
	public HelloModel(String message) {
		this.message = message;
    }	

	public String getMessage() {
		return message;
	}

	public void setMessage(String value) {
		this.message = message;
	}    
}